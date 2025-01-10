from fastapi import FastAPI, BackgroundTasks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import chromedriver_autoinstaller
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Global variables to store WebDriver and extracted data
driver = None
extracted_data = []
@app.on_event("shutdown")
def shutdown_event():
    global driver
    if driver:
        driver.quit()
        driver = None

# Function to initialize the WebDriver (setup for each request)
def init_driver():
    global driver
    if driver is None:
        # Automatically download and install the appropriate chromedriver
        chromedriver_autoinstaller.install()

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Ensure headless mode
        options.add_argument('--no-sandbox')  # Run Chrome in sandbox mode
        options.add_argument('--disable-dev-shm-usage')  # Avoid errors related to shared memory
        driver = webdriver.Chrome(options=options)
    return driver


# Function to extract match details for a specific date
def extract_match_details(date_container):
    match_list_wrapper = date_container.find_next('ul', class_='match-list-wrapper')
    if not match_list_wrapper:
        print("No matches found for this date.")
        return []

    matches = []
    for match in match_list_wrapper.find_all('li', class_='match-card-container'):
        match_data = {}
        team_info_elements = match.find_all('div', class_='team-info')
        match_data['teams'] = []

        for team_info in team_info_elements:
            team_name = team_info.find('span', class_='team-name')
            team_score = team_info.find('span', class_='team-score')
            total_overs = team_info.find('span', class_='total-overs')
            team_logo = team_info.find('img')

            team_logo_url = team_logo['src'] if team_logo else "Logo not found"

            match_data['teams'].append({
                "team_name": team_name.get_text(strip=True) if team_name else "Team name not found",
                "team_score": team_score.get_text(strip=True) if team_score else "Score not found",
                "total_overs": total_overs.get_text(strip=True) if total_overs else "Total overs not found",
                "team_logo_url": team_logo_url
            })

        live_element = match.find('div', class_='result live')
        not_started_element = match.find('div', class_='not-started')

        if live_element:
            match_data['result'] = "Match is live"
            match_data['reason'] = "Match is currently live"
        elif not_started_element:
            start_time_element = not_started_element.find('div', class_='start-text')
            time_element = not_started_element.find('p', class_='time')

            match_data['status'] = "Upcoming"
            match_data['result'] = "Upcoming match"
            match_data['start_time'] = start_time_element.get_text(strip=True) if start_time_element else "Start time not available"
            match_data['reason'] = time_element.get_text(strip=True) if time_element else "Match details not available"
        else:
            result_element = match.find('div', class_='result')
            result_winner = result_element.find('span', style=True) if result_element else None
            match_data['result'] = result_winner.get_text(strip=True) if result_winner else "Result not found"

            reason_element = match.find('span', class_='reason')
            match_data['reason'] = reason_element.get_text(strip=True) if reason_element else "Reason not found"

        scoreboard_url = match.find('a', class_='match-card-wrapper')['href']
        if scoreboard_url:
            if not scoreboard_url.startswith('https://'):
                scoreboard_url = f'https://crex.live{scoreboard_url}'
            match_data['scoreboard_url'] = scoreboard_url
        else:
            match_data['scoreboard_url'] = "Scoreboard URL not found"

        matches.append(match_data)
    return matches

# Function to extract all matches on the current page
def extract_matches_on_page(driver):
    global extracted_data
    all_match_data = []
    try:
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        date_wise_wrap = soup.find('div', id='date-wise-wrap')

        if not date_wise_wrap:
            print("No match data found on this page.")
            return all_match_data

        date_containers = date_wise_wrap.find_all('div', class_='date')
        if not date_containers:
            print("No dates found on this page.")
            return all_match_data

        for date_container in date_containers:
            match_date = date_container.get_text(strip=True)
            print(f"Date: {match_date}")

            matches = extract_match_details(date_container)
            if matches:
                all_match_data.append({
                    "date": match_date,
                    "matches": matches
                })
            else:
                print("No matches for this date.")

        extracted_data = all_match_data  # Update global data here
    except Exception as e:
        print(f"Error while extracting data: {e}")

    return all_match_data

# Function to click pagination buttons (next/previous)
def click_pagination_button(button_class):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, button_class))
        )
        actions = ActionChains(driver)
        actions.move_to_element(button).click().perform()
        print(f"Clicked the '{button_class}' button.")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "date-wise-wrap")))  # Wait until page content is loaded
    except Exception as e:
        print(f"Error clicking '{button_class}' button: {e}")

# Initialize the WebDriver
driver = init_driver()
driver.get("https://crex.live/fixtures/match-list")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "date-wise-wrap")))
# Functions for navigating pages
def click_next_button():
    try:
        next_button_class = ".next-button"
        click_pagination_button(next_button_class)
        print("Moved to the next page.")
    except Exception as e:
        print(f"Error clicking next button: {e}")

def click_previous_button():
    try:
        previous_button_class =  ".prev-button"
        click_pagination_button(previous_button_class)
        print("Moved to the previous page.")
    except Exception as e:
        print(f"Error clicking previous button: {e}")

# FastAPI endpoint to start match data extraction
 

# FastAPI endpoint to get the current page's match data
@app.get("/get_extracted")
async def get_extracted():
    global extracted_data

    extracted_data = []  # Clear previous data
    extracted_data.append(extract_matches_on_page(driver))  # Extract data for the current page
    return {"match_details": extracted_data }

# FastAPI endpoint to go to the next page
@app.get("/next_page")
async def next_page(background_tasks: BackgroundTasks):

    click_next_button()  # Navigate to the next page

    return {"message": "Moved to the next page." }

# FastAPI endpoint to go to the previous page
@app.get("/previous_page")
async def previous_page(background_tasks: BackgroundTasks):

    click_previous_button()  # Navigate to the previous page

    return {"message": "Moved to the previous page." }

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
