import plotly.graph_objects as go
import plotly.io as pio

pio.templates['santander'] = pio.templates['plotly']
tema_santander = pio.templates['santander']

tema_santander.layout.titlefont={'family':'arial', 'size':36}
tema_santander.layout.font ={'family':'arial', 'size':18}

plot_colors = ['#FF3030', '#EC0000','#B80C09', '#960400', '#D6D8DF', '#ABAFC0', '#8188A3', '#141301' ]