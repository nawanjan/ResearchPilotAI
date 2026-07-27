def analysis_agent(results):
    """
    Analysis Agent
    Combines retrieved chunks into one summary.
    """

    summary = ""

    for result in results:
        summary += result.page_content + "\n\n"

    return summary