from scrape_influencers import parse_influencer_table


def test_parse_influencer_table():
    html = '''
    <html>
    <body>
        <table>
            <tr><th>Name</th><th>Followers</th><th>Niche</th><th>Location</th></tr>
            <tr><td>Alice</td><td>10000</td><td>Health</td><td>USA</td></tr>
            <tr><td>Bob</td><td>20000</td><td>Fitness</td><td>Canada</td></tr>
        </table>
    </body>
    </html>
    '''
    data = parse_influencer_table(html)
    assert len(data) == 2
    assert data[0]['name'] == 'Alice'
    assert data[1]['followers'] == '20000'
