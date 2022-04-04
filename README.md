<p align="center"><img width="800" src="./efars/static/img/logo.svg" alt="EFARS Logo"></p>

---

<h2 align='center'>EFARS</h2>
<p align='center'>EFARS stands for Educational File Analysis and Reporting System</p>

---
<p align='center'>

  <img src="https://img.shields.io/badge/Python-3.10.2-blue.svg">
  <a href="https://www.repostatus.org/#wip" target="_blank"><img src="https://www.repostatus.org/badges/latest/wip.svg" alt="Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public."></a>
  <a href="https://www.gnu.org/licenses/gpl-3.0" target="_blank"><img src="https://img.shields.io/github/license/TheNavyInfantry/EFARS" alt="License: GPL-3.0"></a>

</p>

---

[//]: # (<p align='center'>EFARS aims to analyze the training data with data visualization and machine learning and present an analyzed data-oriented report to the user.</p>)


### Project Status
EFARS is still under heavy development. There can be breaking changes, but I am trying to keep them as minimum as possible.

### Installation

**1.** Clone this repository

```
https://github.com/TheNavyInfantry/EFARS.git
```

---
**2.** Change directory to the cloned repository

```
cd EFARS
```

---

**3.** Run with docker-compose.yml

```
docker-compose up
```

After the first run, EFARS will be available at http://localhost:5000/

---

#### Warning:
This project is currently running in a .csv file containing a specific format. If you would like to test it, you can use this 
[mock data](mock_data.csv) file. It will be made more dynamic in future updates.


---
### Project Structure
```
EFARS
│
├─ app.py
├─ config.py
├─ efars
│  ├─ __init__.py
│  ├─ routes.py
│  ├─ static
│  │  ├─ img
│  │  │  ├─ error404.svg
│  │  │  ├─ error404_non_animated.svg
│  │  │  ├─ github.svg
│  │  │  ├─ icon.svg
│  │  │  ├─ logo.svg
│  │  │  └─ process.svg
│  │  ├─ js
│  │  │  ├─ 404_error_animation.js
│  │  │  ├─ core.js
│  │  │  ├─ download.js
│  │  │  ├─ drag_and_drop.js
│  │  │  └─ pdf.js
│  │  └─ styles
│  │     └─ style.css
│  ├─ templates
│  │  ├─ 404.html
│  │  ├─ about.html
│  │  ├─ base.html
│  │  ├─ base_components
│  │  │  ├─ footer.html
│  │  │  ├─ header.html
│  │  │  └─ navbar.html
│  │  ├─ index.html
│  │  ├─ terms.html
│  │  └─ views
│  │     ├─ loading.html
│  │     ├─ result.html
│  │     └─ upload.html
│  ├─ utils.py
│  └─ visualization.py
├─ requirements.txt
├─ mock_data.csv
├─ Dockerfile
├─ docker-compose.yml
├─ Procfile
├─ README.md
├─ LICENSE
└─ .gitignore
```

### Contributing
Merge requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details