# Webscraping: IPEA DATA 

[![Leia em Português](https://img.shields.io/badge/Ler%20em-Português-blue)](README.md)

This project aims to expose my skills in handling **web scraping**. 

More than that, it is about dollar taxes (U$) in Brazilian real (R$) to analyse how some world events contributed to elevating the tax over the years. 

Also, it is a project fully developed using Python and some libraries such as ***pandas*, *bs4* and *Matplotlib***, for analyzing the graphics.

It is supposed to be an analysis that can be replicated and developed using an IDE application to construct a business report for a Financial Market company. 

So, hopefully, it would be useful to you!

## Where to find?

### code_webscraping:
Here you will find the Python code with data extraction from the IPEA Data website. From the extraction until data treatment and their storage in variables to be used in analysis. 

### code_analysis_dollar_taxes

This folder contains the code for 3 analyses, plus the README.md archive with both English and Portuguese versions.

## Resume - Technical Documentation 

### 1) HTTP Request

We are dealing with a website, so we have to handle it as a request. Therefore, the first steps involved retrieving the URL and defining the request function.

In addition, we also implemented a validation step to check if the response was successful (status code 200).

### 2) HTML Parsing

To perform the parsing, which is essentially reading the page, we used BeautifulSoup. It's important here to provide the right information so that the target table or data can be located effectively.

For that reason, **we implemented the standard table lookup using the ID 'grd_DXMainTable' (commonly found in ASP.NET pages with DevExpress)**. If this lookup fails, we ensure the table is still found using an alternative search: class="dxgvTable_Moderno".

### 3) Header Identification

Once the table data is located, the next step is to identify the headers. We attempted this using the class 'dxgvHeader_Moderno'. If not found, we applied an alternative logic to infer the headers from the first few rows of the table.

Since this is a relatively simple website, as a final fallback, we manually **defined the column names as:['Date', 'Exchange Rate - R$ / US$ - commercial - purchase - average'].**

### 4) Data Row Extraction

After the headers were identified, we looked for rows with the class 'dxgvDataRow_Moderno'. If none were found, we tried to identify data rows based on the number of columns and the absence of specific elements.

We then implemented a rule to ensure that the number of columns in each data row matches the number of header columns.

### 5) DataFrame Creation

Using pandas, we built a pandas.DataFrame with the extracted data and the identified column names. We also adjusted the column names slightly to make the analysis step easier.

### 6) Exception Handling

Throughout the code, we handled potential errors using exceptions and printed error logs as needed.
