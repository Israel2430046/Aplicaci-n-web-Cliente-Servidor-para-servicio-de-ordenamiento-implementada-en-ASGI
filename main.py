import urllib.parse
from logic import m_srot

HTML_TEMPLATE = """
<html>
<body>
    <h1>Servicio de ordenamiento Merge-Sort</h1>
    <form method='POST'>
        <input type="text" name="lista" value="{input_val}" placeholder="Ej: 1.5, 9.2, 3.0">
        <button type="submit">Ordenar</button>
    </form>
    {resultado}
</body>
</html>
"""

async def app(scope, receive, send):
    if scope['type'] != 'http':
        return

    method = scope['method']
    response_body = ""

    if method == 'GET':
        response_body = HTML_TEMPLATE.format(input_val="", resultado="")
        
    elif method == 'POST':
        message = await receive()
        body_content = message.get('body', b'').decode()
        params = urllib.parse.parse_qs(body_content)
        cadena_user = params.get('lista', [''])[0]
        
        try:
            lf = [float(x.strip()) for x in cadena_user.split(',') if x.strip()]
            lo = await m_srot(lf)
            cadena_resultado = ", ".join(map(str, lo))

            res_section = f"""
                <div style="background: #eee; padding: 10px; margin-top: 10px;">
                    <strong>Elementos ordenados:</strong><br>
                    {cadena_resultado}
                </div>
            """
            response_body = HTML_TEMPLATE.format(input_val=cadena_user, resultado=res_section)

        except ValueError:
            error_msg = '<p style="color:red;">Error: Usa solo numeros y puntos !!!!!!!!!!!!!!!! NO SOY DIOS PARA ORDENARTE HASTA LA VIDA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!.</p>'
            response_body = HTML_TEMPLATE.format(input_val=cadena_user, resultado=error_msg)

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [[b'content-type', b'text/html']],
    })
    await send({
        'type': 'http.response.body',
        'body': response_body.encode('utf-8'),
    })