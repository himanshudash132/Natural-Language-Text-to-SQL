# from dotenv import load_dotenv
# load_dotenv() ## load all the environemnt variables

# import streamlit as st 
# import os
# import sqlite3

# import google.generativeai as genai

# ## configure our API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Funstion to Load Google Model and provide sql query  as response(means natural lang. to sql query)
# def get_gemini_response(question, prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt[0],question])
#     return response.text 

# ##  Function to retrieve query from the sql database(means above sql query to hit DB)
# def read_sql_query(sql,db):
#     conn=sqlite3.connect(db)  ## create connection
#     cur=conn.cursor()    ## create cursor
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows

# ## Define Your Prompt
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output

#     """


# ]    

# ## Streamlit App

# st.set_page_config(page_title="I can Retrive Any SQL query")
# st.header("Gemini App to Retrive SQL Data")

# question=st.text_input("Input: ",key ="input") #input

# submit=st.button("Ask the question") # submit

# # if submit is clicked
# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)  # response is a sql query
#     data=read_sql_query(response,"student.db")
#     st.subheader("The Response is")
#     for row in data:
#         print(row)
#         st.header(row) # display in st header

        # streamlit run appy.py  
        # pip install -r requirements.txt 

import streamlit as st
import google.generativeai as genai
# streamlit run app3.py

GOOGLE_API_KEY = "AIzaSyB97JQ-JAt0OOhURhdCbqWHYhrATlAzo4s"

genai.configure(api_key = GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')

def main():
    st.set_page_config(page_title="Friday Query Genrator ", page_icon=":robot:")
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>SQL Query Generator</h1>
                <h3>I can generate SQL queries for you!</h3>
                <h4>With Explanation as well!!!</h4>
                <p>This tool is a simple tool that allows you to generate SQL queries based on your prompts.</p>
            </div>
        """,
        unsafe_allow_html=True,
    )
    
    text_input = st.text_area("Enter your Query here in English:")

    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """ 
                Create a SQL Query snippet using the below text:        

                ```
                    {text_input}

                ```
                 I just want a SQL Query.


            """
            #here
            formatted_template=template.format(text_input=text_input)

            st.write(formatted_template)
            response = model.generate_content(formatted_template) # get sql query
            sql_query = response.text 

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
 
            
            expected_output="""
                What would be the expected response of this SQL query snippet:
                        ```
                        {sql_query}
                        ```
                Provide sample tabular Response with no explanation:

            """
            expected_output_formatted=expected_output.format(sql_query=sql_query)
            eoutput=model.generate_content (expected_output_formatted)
            eoutput=eoutput.text




            explanation="""
                Explain this Sql Query:
                        ```
                        {sql_query}
                        ```
                Please provide with simplest of explanation:
            """
            explanation_formatted=explanation.format( sql_query=sql_query)            
            explanation=model.generate_content(explanation_formatted)
            explanation=explanation.text
            

            with st.container():
                st.success("SQL Query Generated Successfully! Here is your Query Below:")
                st.code (sql_query, language="sql")

                st.success("Expected Output of this SQL Query will be:")
                st.markdown(eoutput)

                st.success("Explanation of this SQL Query:")
                st.markdown (explanation)



main()
