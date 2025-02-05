def get_queries(start_date, end_date):
    return {
        'total_user_base': f"""
            SELECT COUNT(DISTINCT iPhoneNumber) as total_user_base
            FROM cdr_maap.mt_cdr_final
            WHERE dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND iDRStatus = 1
        """,
        'promotional_user_base': f"""
            SELECT COUNT(DISTINCT iPhoneNumber) as promotional_user_base
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 3
            AND cdr.iDRStatus = 1
        """,
        'transactional_user_base': f"""
            SELECT COUNT(DISTINCT iPhoneNumber) as transactional_user_base
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 2
            AND cdr.iDRStatus = 1
        """,
        'weekly_user_base': f"""
            SELECT 
                toStartOfInterval(dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                COUNT(DISTINCT iPhoneNumber) as user_base
            FROM cdr_maap.mt_cdr_final
            WHERE dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY week_start, week_end
            ORDER BY week_start
        """
    }