import urllib.parse
from logic import m_srot

HTML_FROM = """
<html>
<body>
    <h1>Servico de ordenamiento Marge-sort"</h1>
    <from method='POST'>
    <input type="text" name="lista" value="{input_val}" placeholder="Ej: 1.5, 9.2, 3.0">
    <button type="submit">Inicar</button>
    </form>
    {resultado}
</body>
</html>
"""



async def app(scope, receive, send):
    if scope['type'] != 'http':
        return

method = scope['method']

if method == 'GET':
    response_body = HTML_TEMPLATE.format(input_val="", resultado_html="")
elif method == 'POST':
    message = await recive()
    body_content = menssage.get('body',b'').decode()
    params = urllib.parse.parse_qs(body_content)
    cadena_user =params.get('lista',[''])[0]
    
    try:
        l





