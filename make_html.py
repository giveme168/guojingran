# -*- coding: UTF-8 -*-
import os
parentdir = os.path.dirname(os.path.abspath(__file__)) + '/'
template_path = 'template.html'

if __name__ == '__main__':
    for dirpath, dirnames, filenames in os.walk(parentdir):
        for filename in filenames:
            if '.md' in filename:
                md_filename = filename[:-3]
                md_path = os.path.join(dirpath, md_filename + '.md')
                html_path = os.path.join(dirpath, md_filename + '.html')
                shell = "pandoc %s --template %s -o %s" % (md_path, parentdir + template_path, html_path)
                os.popen(shell)
