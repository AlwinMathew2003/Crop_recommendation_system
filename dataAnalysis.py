import streamlit as st

@st.cache_data
def app():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib as plt
    from sklearn.model_selection import train_test_split

    st.title("Dataset Visualization")
    st.write("\n")
    st.subheader("Dataset")
    dataset=pd.read_csv("Crop_recommendation.csv")

    st.write(dataset.head())

    st.write("Total number of contents: ",dataset.shape)
    st.subheader("Dataset Information")


    st.write(dataset.describe())

    st.subheader("Total number of null values in the dataset:")
    st.write(pd.DataFrame(dataset.isnull().sum()).transpose())


    # Pairplot
    st.subheader("Pairplot:")
    pairplot_fig = sns.pairplot(dataset)
    st.pyplot(pairplot_fig)

    st.subheader("Feature Correlation")
    corr=dataset.drop(['label'],axis=1).corr()
    corr

    import matplotlib.pyplot as plt
    # Display the correlation heatmap
    st.subheader("Correlation Heatmap:")
    fig_heatmap, ax_heatmap = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cbar=True, cmap='coolwarm', ax=ax_heatmap)
    st.pyplot(fig_heatmap)

    # Display the distribution of each numerical column
    st.subheader("Histograms of Numerical Columns:")
    fig_histograms, axs_histograms = plt.subplots(figsize=(15, 14), nrows=3, ncols=3)
    numerical_columns = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    for col, ax in zip(numerical_columns, axs_histograms.flatten()):
        sns.histplot(dataset[col], bins=20, ax=ax)
        ax.set_title(f"{col} Histogram")
        ax.set_xlabel(None)
    fig_histograms.tight_layout()
    st.pyplot(fig_histograms)

    crop_summary = pd.pivot_table(dataset,index=['label'],aggfunc='mean')
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import random

    # Assuming you have already calculated crop_summary and colorarr

    # Display the crop summary
    st.subheader("Crop Summary:")
    st.write(crop_summary.head())

    colorarr = ['#0592D0', '#Cd7f32', '#E97451', '#Bdb76b', '#954535', '#C2b280', '#808000', '#C2b280', '#E4d008', '#9acd32',
                '#Eedc82', '#E4d96f', '#32cd32', '#39ff14', '#00ff7f', '#008080', '#36454f', '#F88379', '#Ff4500', '#Ffb347',
                '#A94064', '#E75480', '#Ffb6c1', '#E5e4e2', '#Faf0e6', '#8c92ac', '#Dbd7d2', '#A7a6ba', '#B38b6d']

    crop_summary_N = crop_summary.sort_values(by='N', ascending=False)
    # Create a Plotly figure
    fig = make_subplots(rows=1, cols=2)

    # Define data for the top and last nitrogen required crops
    top = {
        'y': crop_summary_N['N'][0:10].sort_values().index,
        'x': crop_summary_N['N'][0:10].sort_values()
    }

    last = {
        'y': crop_summary_N['N'][-10:].index,
        'x': crop_summary_N['N'][-10:]
    }

    # Add traces to the figure
    fig.add_trace(
        go.Bar(top,
            name="Most nitrogen required",
            marker_color=random.choice(colorarr),
            orientation='h',
            text=top['x']),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(last,
            name="Least nitrogen required",
            marker_color=random.choice(colorarr),
            orientation='h',
            text=last['x']),
        row=1, col=2
    )

    # Update trace properties
    fig.update_traces(texttemplate='%{text}', textposition='inside')

    # Update layout
    fig.update_layout(title_text="Nitrogen (N)",
                    plot_bgcolor='white',
                    font_size=12,
                    font_color='black',
                    height=500)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Display the Plotly figure
    st.plotly_chart(fig)



        
    # Assuming you have already calculated crop_summary_P and colorarr


    # Create a Plotly figure
    fig = make_subplots(rows=1, cols=2)
    crop_summary_P = crop_summary.sort_values(by='P', ascending=False)
    # Define data for the top and last phosphorus required crops
    top = {
        'y': crop_summary_P['P'][0:10].sort_values().index,
        'x': crop_summary_P['P'][0:10].sort_values()
    }

    last = {
        'y': crop_summary_P['P'][-10:].index,
        'x': crop_summary_P['P'][-10:]
    }

    # Add traces to the figure
    fig.add_trace(
        go.Bar(top,
            name="Most phosphorus required",
            marker_color=random.choice(colorarr),
            orientation='h',
            text=top['x']),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(last,
            name="Least phosphorus required",
            marker_color=random.choice(colorarr),
            orientation='h',
            text=last['x']),
        row=1, col=2
    )

    # Update trace properties
    fig.update_traces(texttemplate='%{text}', textposition='inside')

    # Update layout
    fig.update_layout(title_text="Phosphorus (P)",
                    plot_bgcolor='white',
                    font_size=12,
                    font_color='black',
                    height=500)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Display the Plotly figure alongside the existing one
    st.plotly_chart(fig)



    # Create a Plotly figure
    fig = make_subplots(rows=1, cols=2)
    crop_summary_K = crop_summary.sort_values(by='K', ascending=False)
    # Define data for the top and last potassium required crops
    top = {
        'y': crop_summary_K['K'][0:10].sort_values().index,
        'x': crop_summary_K['K'][0:10].sort_values()
    }

    last = {
        'y': crop_summary_K['K'][-10:].index,
        'x': crop_summary_K['K'][-10:]
    }

    # Add traces to the figure
    fig.add_trace(
        go.Bar(top,
            name="Most potassium required",
            marker_color=random.choice(colorarr),
            orientation='h',
            text=top['x']),
        row=1, col=1
    )

    fig.add_trace(
        go.Bar(last,
            name="Least potassium required",
            marker_color=random.choice(colorarr),
            orientation='h',
            text=last['x']),
        row=1, col=2
    )

    # Update trace properties
    fig.update_traces(texttemplate='%{text}', textposition='inside')

    # Update layout
    fig.update_layout(title_text="Potassium (K)",
                    plot_bgcolor='white',
                    font_size=12,
                    font_color='black',
                    height=500)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Display the Plotly figure alongside the existing ones
    st.plotly_chart(fig)


    
    # Create a Plotly figure
    fig = go.Figure()

    # Add traces for nitrogen, phosphorous, and potash
    fig.add_trace(go.Bar(
        x=crop_summary.index,
        y=crop_summary['N'],
        name='Nitrogen',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=crop_summary.index,
        y=crop_summary['P'],
        name='Phosphorous',
        marker_color='lightsalmon'
    ))
    fig.add_trace(go.Bar(
        x=crop_summary.index,
        y=crop_summary['K'],
        name='Potash',
        marker_color='crimson'
    ))

    # Update layout
    fig.update_layout(title="N, P, K values comparison between crops",
                    plot_bgcolor='white',
                    barmode='group',
                    xaxis_tickangle=-45)

    # Display the Plotly figure within the Streamlit app
    st.plotly_chart(fig)

    from plotly.subplots import make_subplots

    # Assuming you have already calculated crop_summary

    # Create a Plotly figure
    labels = ['Nitrogen(N)', 'Phosphorous(P)', 'Potash(K)']
    fig = make_subplots(rows=1, cols=5, specs=[[{'type':'domain'}, {'type':'domain'},
                                                {'type':'domain'}, {'type':'domain'},
                                                {'type':'domain'}]])

    # Add traces for each crop
    crops = ['rice', 'cotton', 'jute', 'maize', 'lentil']
    for i, crop in enumerate(crops, start=1):
        crop_npk = crop_summary.loc[crop]
        values = [crop_npk['N'], crop_npk['P'], crop_npk['K']]
        fig.add_trace(go.Pie(labels=labels, values=values, name=crop.title()), 1, i)

    # Update trace properties
    fig.update_traces(hole=0.4, hoverinfo="label+percent+name")

    # Update layout
    fig.update_layout(
        title_text="NPK ratio for Rice, Cotton, Jute, Maize, Lentil",
        annotations=[dict(text='Rice', x=0.06, y=0.8, font_size=15, showarrow=False),
                    dict(text='Cotton', x=0.26, y=0.8, font_size=15, showarrow=False),
                    dict(text='Jute', x=0.50, y=0.8, font_size=15, showarrow=False),
                    dict(text='Maize', x=0.74, y=0.8, font_size=15, showarrow=False),
                    dict(text='Lentil', x=0.94, y=0.8, font_size=15, showarrow=False)]
    )

    # Display the Plotly figure within the Streamlit app
    st.plotly_chart(fig)


    # Define labels for the pie charts
    labels = ['Nitrogen(N)', 'Phosphorous(P)', 'Potash(K)']

    # Define subplots specifications
    specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}], 
            [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]

    # Create a Plotly figure with subplots
    fig = make_subplots(rows=2, cols=5, specs=specs, subplot_titles=['', '', '', '', '']*2, horizontal_spacing=0.1, vertical_spacing=0.15)

    # Define colors for the pie charts
    cafe_colors = ['rgb(255, 128, 0)', 'rgb(0, 153, 204)', 'rgb(173, 173, 133)']

    # Add traces for each fruit
    fruits = ['apple', 'banana', 'grapes', 'orange', 'mango', 'coconut', 'papaya', 'pomegranate', 'watermelon', 'muskmelon']
    for i, fruit in enumerate(fruits, start=1):
        fruit_npk = crop_summary.loc[fruit]
        values = [fruit_npk['N'], fruit_npk['P'], fruit_npk['K']]
        fig.add_trace(go.Pie(labels=labels, values=values, name=fruit.title(), marker_colors=cafe_colors), row=(i-1)//5+1, col=(i-1)%5+1)

    # Update layout
    fig.update_layout(
        title_text="NPK ratio for Fruits",
        annotations=[dict(text='Apple', x=0.06, y=1.08, font_size=15, showarrow=False),
                    dict(text='Banana', x=0.26, y=1.08, font_size=15, showarrow=False),
                    dict(text='Grapes', x=0.50, y=1.08, font_size=15, showarrow=False),
                    dict(text='Orange', x=0.74, y=1.08, font_size=15, showarrow=False),
                    dict(text='Mango', x=0.94, y=1.08, font_size=15, showarrow=False),
                    dict(text='Coconut', x=0.06, y=0.46, font_size=15, showarrow=False),
                    dict(text='Papaya', x=0.26, y=0.46, font_size=15, showarrow=False),
                    dict(text='Pomegranate', x=0.50, y=0.46, font_size=15, showarrow=False),
                    dict(text='Watermelon', x=0.74, y=0.46, font_size=15, showarrow=False),
                    dict(text='Muskmelon', x=0.94, y=0.46, font_size=15, showarrow=False)]
    )

    # Display the Plotly figure within the Streamlit app
    st.plotly_chart(fig)
    import plotly.express as px

    
    # Create the Plotly scatter plot
    crop_scatter = dataset[(dataset['label']=='rice') | 
                      (dataset['label']=='jute') | 
                      (dataset['label']=='cotton') |
                     (dataset['label']=='maize') |
                     (dataset['label']=='lentil')]

    fig = px.scatter(crop_scatter, x="temperature", y="humidity", color="label", symbol="label")

    # Update layout
    fig.update_layout(plot_bgcolor='white')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Display the Plotly scatter plot within the Streamlit app
    st.plotly_chart(fig)

        # Create the Plotly bar chart
    fig = px.bar(crop_summary, x=crop_summary.index, y=["rainfall", "temperature", "humidity"])

    # Update layout
    fig.update_layout(
        title_text="Comparison between rainfall, temperature, and humidity",
        plot_bgcolor='white',
        height=500
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    # Display the Plotly bar chart within the Streamlit app
    st.plotly_chart(fig)



