import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import plotly.express as px


# Custom font style using HTML and CSS with multiple fonts
custom_font_style = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');

        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap');
        body {
            font-family: 'Oswald', 'Playfair Display', 'IBM Plex Sans', sans-serif;
        }
    </style>
"""

# Apply the custom font style
st.markdown(custom_font_style, unsafe_allow_html=True)


@st.cache_data
def load_data():
    data = pd.read_csv("cleaned_file.csv")
    return data

def clusterss(original_data):
    clustering_data = original_data[["BALANCE", "PURCHASES", "CREDIT_LIMIT"]]

    # Correct MinMaxScaler usage
    scaler = MinMaxScaler()
    clustering_data_scaled = scaler.fit_transform(clustering_data)
    clustering_data = pd.DataFrame(clustering_data_scaled, columns=clustering_data.columns)

    kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)
    clusters = kmeans.fit_predict(clustering_data)
    original_data["CREDIT_CARD_SEGMENTS"] = clusters

    original_data["CREDIT_CARD_SEGMENTS"] = original_data["CREDIT_CARD_SEGMENTS"].map({
        0: "Cluster 1",
        1: "Cluster 2",
        2: "Cluster 3",
        3: "Cluster 4",
        4: "Cluster 5"
    })

    return original_data

def recommend_products(selected_credit_limit, clustered_data):
    # Filter data based on selected credit limit
    filtered_data = clustered_data[
        (clustered_data['CREDIT_LIMIT'] >= selected_credit_limit) &
        (clustered_data['CREDIT_LIMIT'] <= selected_credit_limit + 1000)
    ]

    if not filtered_data.empty:
        selected_cluster = filtered_data["CREDIT_CARD_SEGMENTS"].mode().values[0]
        recommendations = get_recommendations(selected_cluster)
        return selected_cluster, recommendations
    else:
        return "No cluster found", ["No recommendations available"]

def get_recommendations(cluster):
    # Add your product recommendation logic here based on the cluster
    products = []
    
    if cluster == "Cluster 1":
        products.append({
            "Name": "Stationary",
            "IMG": "https://imgmedia.lbb.in/media/2023/04/642d50da807623322253cf8f_1680691418800.jpg",  # Replace with actual image URL
            "Visit": "https://scooboo.in/",  # Replace with actual product link
        })
        products.append({
            "Name": "Toys",
            "IMG": "https://content.jdmagicbox.com/comp/def_content/toy-shops/shutterstock-436617280-toy-shops-5-db665.jpg",
            "Visit": "https://www.amazon.in/Toys-Games/b?node=1350380031",
        })
        products.append({
            "Name": "Big Basket",
            "IMG": "https://assets.entrepreneur.com/content/3x2/2000/20160302090451-Great-Grocery-Deals-at-BigBasket-with-Pennyful.jpeg",
            "Visit": "https://www.bigbasket.com/",
        })
    elif cluster == "Cluster 2":
        products.append({
            "Name": "Electric Appliance",
            "IMG": "https://qph.cf2.quoracdn.net/main-qimg-d1d84422f99e43274bf99c3839f0f0fe",
            "Visit": "https://www.amazon.in/Best-Electronic-Gadgets/s?k=Best+Electronic+Gadgets",
        })
        products.append({
            "Name": "Cloths For Men",
            "IMG": "https://assets.vogue.com/photos/5891e0ebb482c0ea0e4db2a8/4:3/w_2560%2Cc_limit/02-lestrange.jpg",
            "Visit": "https://www.beyoung.in/mens-clothing",
        })
        products.append({
            "Name": "Cloths For Women",
            "IMG": "https://d2line.com/thatlook/wp-content/uploads/sites/4/2022/09/women-clothing-fashion-designerstyle-by-d2line.png",
            "Visit": "https://www.ajio.com/shop/women",
        })
    elif cluster == "Cluster 3":
        products.append({
            "Name": "Home Utensils",
            "IMG": "https://cdn.vox-cdn.com/thumbor/lD7Krs0uHXTTvMH8TGvkL-oSyFA=/0x0:5515x3665/1200x800/filters:focal(2317x1392:3199x2274)/cdn.vox-cdn.com/uploads/chorus_image/image/70894045/shutterstock_1042252666.0.jpg",
            "Visit": "https://www.eater.com/23133131/best-kitchen-tools-products-for-cooking-at-home",
        })
        products.append({
            "Name": "Books",
            "IMG": "https://m.economictimes.com/thumb/msid-80119417,width-1200,height-900,resizemode-4,imgsize-288694/books-getty.jpg",
            "Visit": "https://openlibrary.org/",
        })
        products.append({
            "Name": "Pet Store",
            "IMG": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJKjM_YLyTCZsh-xSSnbY4006aPtikQnmiHvGapNWH5CxmL39b2WVnP6QILXte1RZy40o&usqp=CAU",
            "Visit": "https://supertails.com/",
        })
    elif cluster == "Cluster 4":
        products.append({
            "Name": "Trains",
            "IMG": "https://merriam-webster.com/assets/mw/images/article/art-wap-landing-mp-lg/train-3448-72edc8c66df509608c1e13f712a1436e@1x.jpg",
            "Visit": "https://www.ixigo.com/trains/tatkal-railway-reservation?utm_source=bing&utm_medium=paid_search_bing_trains&utm_campaign=train_search_desktop_bing&msclkid=e58a73c19b7d1a067dde16a7ad0e5180&utm_term=train%20bookings&utm_content=Ad%20group%201",
        })
        products.append({
            "Name": "Furniture",
            "IMG": "https://images.adsttc.com/media/images/5f75/0857/63c0/17bc/c900/096d/large_jpg/FLEXFORM_ASOLO_SECTIONAL.jpg?1601505319",
            "Visit": "https://www.ikea.com/in/en/cat/furniture-fu001/",
        })
    elif cluster == "Cluster 5":
        products.append({
            "Name": "Flights",
            'IMG': "https://ojigy.com/self/assets/img/pages/flight_booking_ojigy.jpeg",
            "Visit": "https://www.skyscanner.co.in/routes/gaj/mex/yamagata-to-mexico-city-juarez-international.html?&utm_source=bing&utm_medium=cpc&utm_campaign=IN-Flights-Search-EN-DSA&utm_term=DYNAMIC+SEARCH+ADS&associateID=SEM_GGF_19370_00076&msclkid=9ace8548b34813ef200de02e83ca5c94&gclid=9ace8548b34813ef200de02e83ca5c94&gclsrc=3p.ds",
        })
        products.append({
            "Name": "Cruise",
            "IMG": "https://media.architecturaldigest.com/photos/5654e91c587d37cb3479de02/16:9/w_2560%2Cc_limit/regent-seven-seas-lede.jpg",
            "Visit": "https://www.agoda.com/en-in/search?selectedproperty=319952&city=647&hid=319952&site_id=1914936&tag=26734366-363d-49e8-ac79-4f804513e9c6&device=c&network=o&msclkid=2ade55e5a14d1af3b70930839467a165&pslc=1&ds=g8VhM7wKvkrJ%2B2Br",
        })
        products.append({
            "Name": "Jwellery",
            "IMG": "https://cdn.alromaizan.com/image/upload/v1679132058/media/blog/what-gold-jewellery-to-wear-in-hot-weather.jpg",
            "Visit": "https://www.tanishq.co.in/",
        })
    else:
        return ["No recommendations available"]

    return products


def main():
    st.title("Credit Card Clustering App")

    # Load data
    original_data = load_data()

    # Perform clustering
    clustered_data = clusterss(original_data.copy())

    # # Display original and clustered data
    # st.subheader("Original Data:")
    # st.write(original_data.head())

    # st.subheader("Clustered Data:")
    # st.write(clustered_data.head())

    # # Visualize clusters using Plotly Express
    # fig = px.scatter_3d(
    #     clustered_data,
    #     x="BALANCE",
    #     y="PURCHASES",
    #     z="CREDIT_LIMIT",
    #     color="CREDIT_CARD_SEGMENTS",
    #     title="Credit Card Clusters",
    #     labels={"CREDIT_CARD_SEGMENTS": "Cluster"},
    # )
    # st.plotly_chart(fig)
    st.subheader("Login Page")
    cust_id_input = st.text_input("Enter your CUST_ID:")
    cust_id_list = [cust_id.strip() for cust_id in cust_id_input.split(',')]

    if st.button("Enter"):
        print("CUST_ID List:", cust_id_list)
        if not cust_id_list:
            st.warning("Invalid CUST_ID input. Please enter valid integers.")
        else:
            print("Original Data CUST_ID List:", original_data['CUST_ID'].tolist())
            user_data = original_data[original_data['CUST_ID'].astype(str).isin(cust_id_list)]

            # Check if user_data is not empty
            if not user_data.empty:
                print("Filtered User Data CUST_ID List:", user_data['CUST_ID'].tolist())
                st.subheader("User Data:")
                st.write(user_data)

                # Proceed to recommendation section only if user_data is not empty
                selected_cluster, recommendations = recommend_products(user_data['CREDIT_LIMIT'].mean(), clustered_data)

                st.subheader("Recommended Products:")
                st.write(f"Your credit limit lies in {selected_cluster}")

                for product in recommendations:
                    st.subheader(product["Name"])  # Use lowercase "name" here
                    st.image(product["IMG"], caption=product["Name"], use_column_width=True)
                    st.markdown(f"**IMG:** [{product['Name']}]({product['Visit']})")
            else:
                    st.warning("No data found for the entered CUST_ID. Please check your input.")



    # Credit Limit Selection
    # st.subheader("Select your Credit Limit:")
    # selected_credit_limit = st.slider("Credit Limit", 1000, 27000, 5000, 200)

    # Recommendations based on selected credit limit
    # ... (previous code)

    # Recommendations based on selected credit limit
    # selected_cluster, recommendations = recommend_products(selected_credit_limit, clustered_data)
        # selected_cluster, recommendations = recommend_products(user_data['CREDIT_LIMIT'].mean(), clustered_data)
            
        # st.subheader("Recommended Products:")
        # st.write(f"Your credit limit lies in {selected_cluster}")
        # # st.write(recommendations)

        # # st.subheader("Recommended Products:")
        # # st.write(f"Your credit limit lies in {selected_cluster}")

        # for product in recommendations:
        #     st.subheader(product["Name"])  # Use lowercase "name" here
        #     st.image(product["IMG"], caption=product["Name"], use_column_width=True)
        #     st.markdown(f"**IMG:** [{product['Name']}]({product['Visit']})")

if __name__ == "__main__":
    main()



