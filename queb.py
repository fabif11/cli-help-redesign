import click

@click.command()
@click.option('--help', '-h', is_flag=True)
def queb(help): 

    print('''
    Usage:
        program plot [options] <argument>

    Options:
    SYSTEM
        -h --help   
        -p PATH, --path PATH    
    TEXT
        -t TITLE, --title TITLE    
        -xl XLABEL, --xlabel XLABEL    
        -yl YLABEL, --ylabel YLABEL    
    LOOK
        -c COLOR, --color COLOR     
        -m MARKER, --marker MARKER      
    STATUS
        -s SLEEP, --sleep SLEEP
        '''
    )
