# GW2-SRS
### Guild Wars 2 - System for Raid Study (with applied big data techniques)
-----------------------------------------------------------------------------------
[![gw2](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3b6cc678-b1b3-4c10-9c25-e278bd301dd5/d8u83ma-186a112b-4859-4613-91b6-dffed9d8ca7a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNiNmNjNjc4LWIxYjMtNGMxMC05YzI1LWUyNzhiZDMwMWRkNVwvZDh1ODNtYS0xODZhMTEyYi00ODU5LTQ2MTMtOTFiNi1kZmZlZDlkOGNhN2EucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.uL8HBogU4dH7WKAibcZ7QuMN-r4-X1LVeIzpe99jJ2M "gw2")](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/3b6cc678-b1b3-4c10-9c25-e278bd301dd5/d8u83ma-186a112b-4859-4613-91b6-dffed9d8ca7a.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzNiNmNjNjc4LWIxYjMtNGMxMC05YzI1LWUyNzhiZDMwMWRkNVwvZDh1ODNtYS0xODZhMTEyYi00ODU5LTQ2MTMtOTFiNi1kZmZlZDlkOGNhN2EucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.uL8HBogU4dH7WKAibcZ7QuMN-r4-X1LVeIzpe99jJ2M "gw2")

-----------------------------------------------------------------------------------
#### Objectives
- Analyze data from raid logs generated by the [ARC DPS](http://www.deltaconnected.com/arcdps/ "ARC DPS") tool.
- Understanding of results by analyzing fails and kills on each boss.
- Apply Big Data techniques and learn throughout the whole process.
-----------------------------------------------------------------------------------
# PoI (Points of Interest)


**Project Contents**
- [Route](#route)
  - [Extraction](#extract-of-data)
  - [Transform](#transforming-data)
- [Tools Used](#tools-used)

### Route
##### Extract of Data
- Getting data from ARC Dps tool as .zevtc files (log files).
- Parsing .zevtc files to csv/json using [Elite Insights](https://github.com/baaron4/GW2-Elite-Insights-Parser "Elite Insights") tool from GitHub user [baaron4](https://github.com/baaron4 "baaron4").

##### Transforming Data
- Working with Microsoft Excel and [CSVed](https://csved.sjfrancke.nl/ "CSVed") to get usefull and clean .csv files for data management.
- Use of Jupyter Notebooks, Python and Pandas for data analysis.
- Use of python libraries to create KPIs: Matplotlib, Seaborn...

### Tools used

[EditorMD](https://pandao.github.io/editor.md/en.html "EditorMD") from Pandao
VS Code
