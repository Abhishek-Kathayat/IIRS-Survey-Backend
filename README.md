# IIRS Survey API in Django

### Introduction

A Django REST API for the IIRSSurveyApp Android App. The API makes uses of Spatialite-SQLite as database. Main task of the API is to read the ArcGIS Shapefile available and locate the coordinates recieved from the frontend in the shapefile polygons and return the corresponding data associated with that location. Data recieved from the frontend is stored in PointField in the database.<br/>
<br/>
This API is a part of the Android Application I created in Summer Internship Programme at Indian Institute of Remote Sensing (IIRS), Dehradun. The link to the Android Application project is provided below : <br/><br/>
[IIRS Survey App](https://github.com/Abhishek-Kathayat/IIRSSurveyApp)
