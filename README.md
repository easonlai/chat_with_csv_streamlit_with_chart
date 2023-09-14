# Chat with your CSV (with chart visualization)

In this repository, you will find an example code for creating an interactive chat experience that allows you to ask questions about your CSV data. The code uses [Pandas Dataframe Agent](https://python.langchain.com/docs/integrations/toolkits/pandas) from [LangChain](https://python.langchain.com/docs/get_started/introduction) and a [GPT model](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models) from [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview) to interact with the data. To make the chat more versatile, I incorporated some prompt engineering techniques that instruct the GPT model to use the popular data visualization library, [Matplotlib](https://matplotlib.org/stable/index.html), to create charts based on your queries. The chart is then saved and visualized using the [Streamlit](https://streamlit.io/) frontend interface. This feature can create any [type of chart](https://matplotlib.org/stable/plot_types/index.html) (pie, line, scatter, etc.) as long as you provide clear instructions. Additionally, the code can also return the dataframe as a table or provide a straightforward answer.

To run this Streamlit web app
```
streamlit run run.py
```

Sample query to give a straightforward answer.
![alt text](https://github.com/easonlai/chat_with_csv_streamlit_with_chart/blob/main/git-images/git-image-1.png)

Sample query to show the result in the table.
![alt text](https://github.com/easonlai/chat_with_csv_streamlit_with_chart/blob/main/git-images/git-image-2.png)

Sample query to show the result in a bar chart.
![alt text](https://github.com/easonlai/chat_with_csv_streamlit_with_chart/blob/main/git-images/git-image-3.png)

Sample query to show the result in a pie chart.
![alt text](https://github.com/easonlai/chat_with_csv_streamlit_with_chart/blob/main/git-images/git-image-4.png)

Enjoy!