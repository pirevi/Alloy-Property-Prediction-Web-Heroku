# Multi Component Alloy Property Prediction Web-App

I had trained surrogate ML model on DFT dataset of binary alloys sourced from Materials Project database using pymatgen library. The details about the complete pipeline and findings is available in my research publication (under review). I will update the link to the paper here once its published. Here I have deployed the trained model in form of a web application using Flask and Heroku. The application accepts any Alloy Formula and predicts it 9-Elastic Constants(Cij) along with Bulk Modulus(B), Shear Modulus(G) and Poissons Ratio(PR). 

#### [Click Here](https://alloy-property-predict.herokuapp.com/) to go to the Heroku Web-App

## Web-App-UI:

<img src="/UI_web_app.png" alt="Web-App User Interface"/>
