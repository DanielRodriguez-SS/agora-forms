import frontend.styling as css

def render_availability(shop_availability:dict) -> str:
    html = ''
    for item in shop_availability:
        html += f'''<div style={css.MORE_DETAILS}>
                        {item}: {shop_availability[item]}
                    </div>'''
    return html