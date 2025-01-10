
<a id="readme-top"></a>

<!-- Badges Section -->
<div align="center">

  <h1>Real time Matches Data Scraper</h1>


  <!-- Shields -->
  <p>
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping/network/members">
      <img src="https://img.shields.io/github/forks/Nikhil-9981/AI_Agent_for_CSV_files?style=for-the-badge" alt="Forks">
    </a>
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping/stargazers">
      <img src="https://img.shields.io/github/stars/Nikhil-9981/AI_Agent_for_CSV_files?style=for-the-badge" alt="Stars">
    </a>
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping/issues">
      <img src="https://img.shields.io/github/issues/Nikhil-9981/AI_Agent_for_CSV_files?style=for-the-badge" alt="Issues">
    </a>
  </p>

  <!-- Description -->
  <p>
   This application automates the process of gathering cricket match information from a website. It allows users to view details about matches, navigate between pages of match listings, and display the collected information through a user-friendly web interface.
  </p>

  <!-- Action Links -->
  <p>
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping" style="text-decoration:none;">
      <strong>Explore Documentation »</strong>
    </a>
    <br />
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping">View Demo</a> ·
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping/issues/new?labels=bug&template=bug-report---.md">Report Bug</a> ·
    <a href="https://github.com/Nikhil-9981/Real_time_cricket_Scraping/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- Social Media Section -->
<div align="center">
  <a href="https://www.linkedin.com/in/nikhil9981/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Nikhil%20Kumar%20Singh-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
  </a>


 <hr />


</div>





<!-- TABLE OF CONTENTS -->
<details>
  <summary><h3>Table of Contents </summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#Follow  up Questions">Optional Features </a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
 - ** The deployed website is currently facing some issues and is not functioning properly, but it is running fine locally. Please consider this as I was unable to complete the deployment due 
  to time constraints, though I am actively working on resolving it**

  This application automates the process of gathering cricket match information from a website. It allows users to view details about matches, navigate between pages of match listings, and display the collected information through a user-friendly web interface.

 ### 🚀 Key Features:

- **Automated Data Extraction**: The application automatically gathers detailed information about cricket matches, including teams, scores, match status, and more.

- **Paginated Navigation**: Users can easily navigate through multiple pages of match listings to access data for different dates or events.

- **Real-time Data Display**: Extracted match details are displayed in a structured format on a web interface, allowing users to view the latest information in real time.

- **User-friendly Interface**: The application provides a simple and interactive web interface for users to access match data, making it easy to view and navigate without technical expertise.
With this project, you can automate  the process of gathering and structuring data, enabling smarter and more efficient decision-making.

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>




## Built With

### Technologies and Tools Used


* [![FastAPI](https://img.shields.io/badge/FastAPI-blue)](https://fastapi.tiangolo.com/)
* [![Selenium](https://img.shields.io/badge/Selenium-yellowgreen)](https://www.selenium.dev/)
* [![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-lightgreen)](https://www.crummy.com/software/BeautifulSoup/)
* [![Docker](https://img.shields.io/badge/Docker-lightblue)](https://www.docker.com/)
* [![Jinja2](https://img.shields.io/badge/Jinja2-lightred)](https://palletsprojects.com/p/jinja/)
* [![Render](https://img.shields.io/badge/Render-lightgrey)](https://render.com/)





<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to set up the project and begin using the **AI Agent for CSV files**.

### 🔧 Prerequisites

   Before you begin, ensure that the following are installed:

1. **Python (version 3.7 or higher)**
   The project is developed in Python, so you will need to have Python 3.7 or later installed.
   You can download Python from the official website:
   ➡️ [Python Downloads](https://www.python.org/downloads/)

2. **Docker (Optional)**
   If you prefer running the project in a containerized environment, you will need Docker installed:
   ➡️ [Docker Download](https://www.docker.com/get-started)



4. **Text Editor or IDE**
   You will need a text editor or integrated development environment (IDE) for Python development. Recommended options include:

   - **[Visual Studio Code (VS Code)](https://code.visualstudio.com/Download)**
   - **[PyCharm](https://www.jetbrains.com/pycharm/download/)**

---


### Installation

1. **Clone the Repository**:  <br>
   Run the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/Nikhil-9981/Real_time_cricket_Scraping
   ```

2. **Create a virtual environment**: <br>
    Create a new virtual environment by running:
      ```bash
      python -m venv myenv
      ```

      (You can replace myenv with your preferred environment name)


      •  To activate the environment:
      ```bash
      myenv/Scripts/activate
      ```
3. **Install requirements** : <br>
Once the virtual environment is activated, install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```





6. **Run app locally by FastAPI**  : <br>
To start the app using FastAPI, run:

    ```bash
    uvicorn app.main:app --reload
    ```

      **--------------------------------------OR---------------------------------------------------**

  **Optional** : <br>
  1. **Check docker is installed  or not** :
  ```bash
    docker images
  ```
  2. **Build docker image using this command**  : <br>
     To build the Docker image, use the following command:
  ```bash
    docker build -t  selenium_scraper .
  ```
  (You can replace aiagent with your preferred environment name.)

  3. **Run docker image locally**  : <br>
    Run the following command to start the Docker image:

  ```bash
   docker run -it -p 8000:8000 selenium_scraper
  ```

4. If you want to deploy docker image on Render follow this link :
- **[Deployment on Render documentation](https://docs.render.com/)**
     🎥 [Youtube Guide](https://youtu.be/Qb7tNtIEpcA?si=77bQeRZLVesm_AZJ)







<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>









## Follow-up Questions

1. **Why did you choose the specific scraping approach you used?**
   - The current scraping approach leverages Selenium for dynamic content handling and BeautifulSoup for parsing, ensuring robustness in dealing with web pages that load content asynchronously or via JavaScript. This combination offers flexibility in extracting data from structured or complex web layouts.

2. **How can we further optimize the resource usage of your system?**
   - To optimize resource usage, we can:
     - Consider using headless browsing in Selenium to reduce memory overhead.
     - Implement more efficient data fetching strategies, such as selective scraping (only requesting data that is necessary).
     - Introduce caching mechanisms to avoid redundant data fetching.
     - Use async features where applicable to handle multiple web requests concurrently.

3. **Can the time consumption of your codebase be further reduced?**
   - Yes, time consumption can be reduced by:
     - Implementing parallel scraping using threading or multiprocessing to scrape data from multiple sources concurrently.
     - Reducing the wait times in Selenium by refining the logic for element loading or using more advanced wait strategies.
     - Optimizing the parsing logic by focusing only on the elements needed and avoiding unnecessary traversals of the DOM.

4. **If given more time, what changes would you make to the codebase and why?**
   - If given more time, the following changes would be made:
     - Refactor the code into modular components to enhance maintainability and make it easier to add new features.
     - Implement advanced error handling and logging mechanisms to improve the reliability of the system in production.
     - Add user authentication and session management to allow for persistent connections.
     - Optimize the scraping logic to handle dynamic content more efficiently and minimize the time spent on web page loading.
     - Include more interactive features in the frontend (e.g., real-time updates of data) to enhance user experience.
     - Integrate Celery for background task management to handle data extraction or processing asynchronously, improving the scalability of the system.




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top"><strong>Back to top</strong></a>)</p>


 #
<div style="text-align: center; font-size: 36px; font-weight: bold; color: #4CAF50; text-transform: uppercase; letter-spacing: 3px; animation: slideIn 2s ease-in-out;">
    Get in Touch
</div>

<div style="text-align: center; font-size: 20px; font-style: italic; color: #333; margin-top: 10px; animation: fadeIn 2s ease-in-out;">
    I’d love to hear from you!
</div>

<div style="text-align: center; font-size: 18px; color: #FF6347; margin-top: 20px;">
    Nikhil Kumar Singh<br>
    <a href="https://www.linkedin.com/in/nikhil9981/" style="color: #4CAF50; text-decoration: none; font-weight: bold;">@nikhil9981</a><br>
    <a href="mailto:rathaurnikhil14@gmail.com" style="color: #4CAF50; text-decoration: none; font-weight: bold;">rathaurnikhil14@gmail.com</a><br><br>
    
</div>

<p align="right" style="font-size: 18px; color: #4CAF50;">
    (<a href="#readme-top" style="color: #FF6347; font-weight: bold;">Back to top</a>)
</p>



<div style="text-align: center; font-size: 60px; font-weight: bold; color: #FF6347; text-transform: uppercase; letter-spacing: 5px; animation: bounce 1.5s ease-in-out infinite;">
    THANK YOU!
</div>

<div style="text-align: center; font-size: 24px; font-style: italic; color: #555; animation: fadeIn 2s ease-in-out;">
    Your time and attention mean the world! ✨
</div>

 
