import PySimpleGUI as sg
from emoji import emojize
from config import *

sg.theme(theme)

LINK_TAB_LAYOUT = [
    [
        sg.Frame('', [
                [
                    sg.Text('Inserisci un link', pad=(10, 10), font=(fontFamily, fontSize))
                ],
                [
                    sg.Input(key='-LINK-', pad=(10, 10), font=fontFamily + ' ' + str(fontSize))
                ],
                [
                    sg.Button('Converti', key='-LINK_BUTTON-', pad=(10, 10), font=(fontFamily, int(fontSize/2)))
                ],
                [
                    sg.Image(key='-LINK_IMAGE-', pad=(10, 10)),
                    sg.Frame('', [
                        [
                            sg.Text('Titolo: ', font=fontFamily + ' ' + str(fontSize)),
                            sg.Text(key='-LINK_TITLE-', font=fontFamily+ ' ' + str(int(fontSize / 2)), size=(40, None))
                        ],
                        [
                            sg.Text('Durata: ', font=fontFamily + ' ' + str(fontSize)),
                            sg.Text(key='-LINK_VIDEO_LENGTH-', font=fontFamily + ' ' + str(fontSize))
                        ],
                        [
                            sg.Text('Peso (Video): ', font=fontFamily + ' ' + str(fontSize)),
                            sg.Text(key='-LINK_VIDEO_AND_AUDIO_SIZE-', font=fontFamily + ' ' + str(fontSize))
                        ],
                        [
                            sg.Text('Peso (Audio): ', font=fontFamily + ' ' + str(fontSize)),
                            sg.Text(key='-LINK_AUDIO_SIZE-', font=fontFamily + ' ' + str(fontSize))
                         ]
                    ],
                    key='-LINK_INFO-',
                    pad=(10, 10), 
                    visible=False,
                    expand_x=True
                    ),
                ],
                [
                    sg.Button('Download', visible=False, pad=(10, 10), font=fontFamily + ' ' + str(fontSize), key='-LINK_DOWNLOAD-'),
                    sg.Button('Reset', visible=False, pad=(10, 10), font=fontFamily + ' ' + str(fontSize), key='-LINK_RESET-')
                ],
                [
                    sg.ProgressBar(visible=False, max_value=100, orientation='horizontal', style='classic', key='-LINK_PROGRESSBAR-', expand_x=True, expand_y=True)
                ]
            ], 
            size=(WIDTH, HEIGTH/100*90),
            )
        ]
]

heading = ['Titolo', 'Durata', 'Peso Video & Audio', 'Peso Audio']

SEARCH_TAB_LAYOUT = [
        [
        sg.Frame('', [
                [
                    sg.Text('Inserisci parole chiave', pad=(10, 10), font=fontFamily + ' ' + str(fontSize))
                ],
                [
                    sg.Input(key='-SEARCH-', pad=(10, 10), font=fontFamily + ' ' + str(fontSize)),
                ],
                [
                    sg.Button('Cerca', key='-SEARCH_BUTTON-', pad=(10, 10), font=fontFamily + ' ' + str(int(fontSize/2)))
                ],
                [
                    sg.Table(
                        values = [],
                        headings=heading,
                        enable_events=True,
                        key='-SEARCH_TABLE-',
                        expand_x=True,
                        expand_y=True,
                        font=fontFamily + ' ' + str(int(fontSize/2)),
                        pad=(10, 10),
                        hide_vertical_scroll=True
                        )
                ],
                [
                    sg.Button('Download', visible=False, pad=(10, 10), font=fontFamily + ' ' + str(fontSize), key='-SEARCH_DOWNLOAD-'),
                    sg.Button('Reset', visible=False, pad=(10, 10), font=fontFamily + ' ' + str(fontSize), key='-SEARCH_RESET-')
                ],
                [
                    sg.ProgressBar(visible=False, max_value=100, orientation='horizontal', style='classic', key='-SEARCH_PROGRESSBAR-', expand_x=True, expand_y=True)
                ]
            ], 
            size=(WIDTH, HEIGTH/100*90),
            )
        ]
    ]

FILE_TAB_LAYOUT = [
    [

    ]
]

MAIN_WINDOW_LAYOUT = [
   [
        sg.Frame('', [
            [sg.TabGroup([
                [sg.Tab('Link', LINK_TAB_LAYOUT, key='-LINK_TAB-')],
                [sg.Tab('Ricerca', SEARCH_TAB_LAYOUT, key='-SEARCH_TAB-')],
                [sg.Tab('File', FILE_TAB_LAYOUT, key='-FILE_TAB-')],
            ],
            tab_location='lefttop',
            border_width=0,
            font=fontFamily + ' ' + str(fontSize),
            )]
        ], 
        size=(WIDTH, HEIGTH / 100 * 93),
        border_width=0,
        )
    ],
    [
        sg.Frame('', [
            [
                sg.Frame('', [
                    [
                        sg.Button(
                            'Quit', 
                            font=(fontFamily, int(fontSize/2)),
                            button_color='darkred',
                            key='-QUIT-'
                            ),
                        sg.Button(
                            emojize(':gear:'),
                            font=(fontFamily, int(fontSize/2)),
                            key='-SETTINGS-'
                            ),
                        sg.Button(
                            emojize(':bust_in_silhouette:'),
                            font=(fontFamily, int(fontSize/2)),
                            key='-ABOUT-'
                            ),  
                    ]   
                ],
                border_width=0,
                ),
                sg.Frame('', [
                    [
                        sg.Radio('Video & Audio', '-FORMAT-', key='VA', default=True, font=(fontFamily, int(fontSize/2))),
                        sg.Radio('Audio', '-FORMAT-', key='A', font=(fontFamily, int(fontSize/2)))
                    ]   
                ],
                border_width=0,
                )
            ]
        ],
        size=(WIDTH, HEIGTH / 100 * 7),
        border_width=0
        )
    ]
]