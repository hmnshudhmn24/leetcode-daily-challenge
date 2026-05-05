import pandas as pd

def friendly_movies(tv_program: pd.DataFrame, content: pd.DataFrame) -> pd.DataFrame:
    df = tv_program.merge(content, on='content_id')
    mask = (
        (df['Kids_content'] == 'Y') &
        (df['content_type'] == 'Movies') &
        (df['program_date'].dt.strftime('%Y-%m') == '2020-06')
    )
    return df[mask][['title']].drop_duplicates()
