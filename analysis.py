
# Complex analysis template

template = """
    The following text contains cyber security and OSINT news articles. Your tasks are:

    1. **Factor Analysis**:
       - Identify key factors or elements from each article.
       Example: 
       Factor: A new ransomware named "CyberLock" has been discovered.

    2. **Deduction**:
       - Deduce the implications of each factor.
       Example:
       Deduction: "CyberLock" ransomware could potentially target major corporations, leading to data breaches.

    3. **Conclusion**:
       - Based on the deduction, conclude with a task, request for information, constraint, or another factor for second-level analysis.
       Example:
       Conclusion: Implement preventive measures against "CyberLock" and monitor network traffic for any unusual activities.

    For factors that lead to a second-level analysis:
    - Repeat the process of factor analysis, deduction, and conclusion to delve deeper into the implications and required actions.

    Provided Articles:
    {news_articles}

    YOUR STRUCTURED ANALYSIS:

    From the provided articles, it's evident that [Factor]. This implies that [Deduction]. As a result, the actionable insight is to [Conclusion: Task/Request/Constraint]. Further, upon second-level analysis, [Second-level Factor] suggests that [Second-level Deduction], leading to the recommendation to [Second-level Conclusion: Task/Request/Constraint].
"""


prompt = PromptTemplate(
    input_variables=["news_articles"],
    template=template,
)
