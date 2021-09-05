from lingx.utils.lx import get_sentence_lx

def visualize_text_complexity(
                                input, 
                                nlp, 
                                color_category = "orange", # chose "grey", "blue" or "orange"
                                html_output = "text.html",
                                complexity_type = "idt"
                                ):

    intensity_grey=[[224,224,224], [192,192,192], [160,160,160], [128,128,128], [96,96,96], [64,64,64], [32,32,32], [32,32,32], [32,32,32]]
    intensity_blue=[[153,153,255], [102,102,255], [51,51,255], [0,0,255], [0,0,204], [0,0,153], [0,0,102], [0,0,102], [0,0,102]]
    intensity_orange=[[225,229,255], [255,204,153], [255,178,102], [255,153,51], [255,128,0], [204,102,0], [153,76,0], [102,51,0], [51,25,0]]


    tokens_scores_list, _ = get_sentence_lx(input, nlp, result_format="segment", complexity_type = complexity_type, aggregation_type="sum")

    if color_category == "orange":
        intensity = intensity_orange
    elif color_category == "blue":
        intensity = intensity_blue
    elif color_category == "grey":
        intensity = intensity_grey
    else:
        raise Exception('Chose either "grey", "blue" or "orange" for `color_category` argument.') 


    html = ""
    html += "<p>\n"

    for token, score in tokens_scores_list:
        if score > 8:
            score = 8
        html += '<span style="color: rgb('+str(intensity[score][0])+','+str(intensity[score][1])+','+str(intensity[score][2])+')">'+token+ ' '+ '</span>\n'
    html += "</p>\n"


    htmlfile = open(html_output, 'w')
    htmlfile.write(html)
    htmlfile.close()