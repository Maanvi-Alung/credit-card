# credit-card

This is an application where  we analyzed the csv file which holds details of credit card users and then provided them whith the information what they can buy accordingly.

Sure, here is an explanation of the code in 10 points:

1. **Library Imports and Custom Fonts**:
    - The script imports necessary libraries such as pandas, numpy, scikit-learn for machine learning, Streamlit for web application creation, and Plotly for visualizations.
    - Custom font styles are defined and applied using HTML and CSS within the Streamlit app.

2. **Data Loading with Caching**:
    - The `load_data()` function loads the data from a CSV file ("cleaned_file.csv") using pandas.
    - The `@st.cache_data` decorator ensures the data is loaded only once and cached for future use, improving performance.

3. **Data Clustering**:
    - The `clusterss()` function takes the original data and selects specific columns for clustering.
    - Data is scaled using `MinMaxScaler` to normalize the values.
    - KMeans clustering is performed with 5 clusters, and the results are added to the original data with meaningful labels ("Cluster 1", "Cluster 2", etc.).

4. **Product Recommendation Based on Clusters**:
    - The `recommend_products()` function filters the clustered data based on a selected credit limit and determines the most frequent cluster within the filtered data.
    - It calls `get_recommendations()` to get product recommendations for the identified cluster.

5. **Generating Recommendations**:
    - The `get_recommendations()` function returns a list of product recommendations based on the identified cluster. Each product includes a name, image URL, and a visit link.

6. **Streamlit Web App Layout**:
    - The `main()` function sets up the Streamlit app, including the title and input fields for user interaction.
    - Users enter their customer IDs, and the app processes the input to filter the relevant user data.

7. **User Data Display**:
    - If valid customer IDs are entered, the corresponding user data is displayed in a table format.
    - If no data is found for the entered IDs, a warning message is shown.

8. **Displaying Recommendations**:
    - Based on the user's credit limit, product recommendations are generated and displayed.
    - For each recommended product, the name, image, and a clickable link are shown.

9. **Error Handling**:
    - The code includes error handling to display warnings for invalid customer ID inputs or if no data is found for the entered IDs.

10. **App Execution**:
    - The script ends by calling the `main()` function if the script is run directly, initializing the Streamlit app.

This code provides a complete workflow for loading data, performing clustering, and providing personalized product recommendations based on the user's credit limit and clustering results. The Streamlit app allows for interactive user input and displays the relevant data and recommendations dynamically.

Following are the snapshots:-

![image](https://github.com/Maanvi-Alung/credit-card/assets/132609092/4ce6ff2f-cf12-4350-a855-b4a8e563bf98)

![image](https://github.com/Maanvi-Alung/credit-card/assets/132609092/b9e4f88f-803c-4b2b-b0f6-9e0ffa8299a0)

![image](https://github.com/Maanvi-Alung/credit-card/assets/132609092/07791c17-60aa-43cb-8e74-2fa1c9b4c610)

![image](https://github.com/Maanvi-Alung/credit-card/assets/132609092/acef5edf-5b42-4d6f-a4e8-97c9b80c7dd8)



