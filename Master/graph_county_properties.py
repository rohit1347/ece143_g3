# Author - Himanshu Gupta - h5gupta@ucsd.edu
from import_xls import *


def graph_year_property(h, p_no=0):
    '''
    Creates bar graphs with slider for years from 2006 to 2017 for a particular parameter

    Arguments:
        h{dict} -- Dictionary with filled dataframes

    Keyword Arguments:
        p_no{int} -- Parameter to be plotted
    '''
    assert isinstance(p_no, int)
    assert p_no >= 0 and p_no <= 6
    assert isinstance(h, dict)

    output_file("bars.html")
    xlabels = []
    c = apta_utils()  # An instance of the class "apta_utils"

    for key, value in c.cities.items():
        # labels used for the x-axis in the form "State: City"
        xlabels.append(key + ': ' + value[0])

    yr_ind = 0

    p_values = []
    for yr_ind in range(12):
        i = 0
        p_value = [0 for x in range(18)]
        for state, city_list in h.items():
            city_p = [d.get(str(c.col_index_names1000[p_no]))
                      for d in city_list]
            a = np.array(city_p)
            if p_no == 0:
                a = a / 1000000  # To get "Population" in millions
            if p_no == 5:
                a = a / 1000  # To get "Unlinked passenger trips" in thousands
            col = 0
            for row in a:
                if col == 1:  # To get values of only the 1st city for each state
                    break
                p_value[i] = row[yr_ind]
                col = col + 1
            i = i + 1
        # List containing values corresponding to 1st city for each state
        p_values.append(p_value)

    alldat = {}
    syear = h['CA'][0].index[0]
    nyears = len(h['CA'][0].index)
    for ix, yy in enumerate(range(syear, syear + nyears)):
        alldat[str(yy)] = p_values[ix]
    source_available = ColumnDataSource(data=alldat)
    source_visible = ColumnDataSource(
        data=dict(counties=xlabels, pvalue=p_values[0]))
    TOOLS = "pan,wheel_zoom,reset,hover,save"
    p = figure(x_range=xlabels, plot_height=450, plot_width=800,
               title=c.col_index_names1000[p_no], toolbar_location=None, tools=TOOLS)
    p.vbar(x='counties', top='pvalue', source=source_visible,
           width=0.4, alpha=0.7, color='#643fe0')
    p.x_range.range_padding = 0.1
    p.title.align = 'center'
    p.title.text_font_size = '14pt'
    if p_no == 0:
        p.yaxis.axis_label = 'In millions'
    if p_no == 5:
        p.yaxis.axis_label = 'In thousands'
    p.yaxis.axis_label_text_font_size = '12pt'
    p.yaxis.major_label_text_font_size = '12pt'
    p.xaxis.major_label_orientation = 3.14/4
    p.xaxis.major_label_text_font_size = '12pt'
    p.axis.minor_tick_line_color = 'black'
    p.outline_line_color = 'black'
    slider = Slider(start=syear, end=syear+nyears-1,
                    value=syear, step=1, title="Year", bar_color='#643fe0', align="center")
    slider.callback = CustomJS(
        args=dict(source_visible=source_visible,
                  source_available=source_available), code="""
        var selected_year = cb_obj.value;
        // Get the data from the data sources
        var data_visible = source_visible.data;
        var data_available = source_available.data;
        // Change y-axis data according to the selected value
        data_visible.pvalue = data_available[selected_year];
        // Update the plot
        source_visible.change.emit();
    """)
    hover = p.select_one(HoverTool)
    property = h['CA'][0].columns[p_no]
    hover.tooltips = [("County", "@counties"), (property,
                                                "$y")]
    show(column(p, widgetbox(slider),))
