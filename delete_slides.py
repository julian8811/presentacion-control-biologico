import re

def main():
    file_path = '/home/julian/diapos_control/Presentacion_Control_Biologico.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Delete Slide 17 and 18 sections
    # Using regex to match from <!-- ===== SLIDE 17 to the end of SLIDE 18
    # We will match from <!-- ===== SLIDE 17 up to just before <!-- ===== SLIDE 19
    pattern = re.compile(r'<!-- ===== SLIDE 17:.*?(?=<!-- ===== SLIDE 19)', re.DOTALL)
    content = pattern.sub('', content)

    # 2. Rename SLIDE 19 to 17
    content = content.replace('<!-- ===== SLIDE 19: Referencias ===== -->\n  <!-- ===== SLIDE 19: Referencias ===== -->', '<!-- ===== SLIDE 17: Referencias ===== -->')
    content = content.replace('<!-- ===== SLIDE 19: Referencias ===== -->', '<!-- ===== SLIDE 17: Referencias ===== -->')
    content = content.replace('data-slide="19"', 'data-slide="17"')
    
    # 3. Change all " / 19" to " / 17" in slide-number
    content = content.replace(' / 19</span>', ' / 17</span>')
    content = content.replace('19 / 17</span>', '17 / 17</span>')
    
    # 4. Update sidebar
    # Remove li for 17 and 18
    sidebar_17_pattern = re.compile(r'<li><a class="sidebar-link" data-slide-link="17".*?</li>\n', re.DOTALL)
    content = sidebar_17_pattern.sub('', content)
    sidebar_18_pattern = re.compile(r'<li><a class="sidebar-link" data-slide-link="18".*?</li>\n', re.DOTALL)
    content = sidebar_18_pattern.sub('', content)
    
    # Change 19 to 17 in sidebar
    content = content.replace('data-slide-link="19"', 'data-slide-link="17"')
    content = content.replace('<span class="link-num">19</span>', '<span class="link-num">17</span>')
    content = content.replace('19 diapositivas</p>', '17 diapositivas</p>')
    
    # 5. Update javascript state
    content = content.replace('totalSlides: 19,', 'totalSlides: 17,')
    content = content.replace('1/19</span>', '1/17</span>')
    # and any dynamic text replacement in JS:
    content = content.replace('`/19`', '`/17`')
    content = content.replace('"/19"', '"/17"')
    content = content.replace("'/19'", "'/17'")
    content = content.replace('${state.totalSlides}', '17') # just in case
    # actually JS might have: textContent = `${state.currentSlide}/19`
    content = content.replace('/19`;', '/17`;')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    main()
