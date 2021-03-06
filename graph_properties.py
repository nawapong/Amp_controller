__author__ = 'Kyle Vitautas Lopin'


class GraphProps(object):

    def __init__(self):

        self.amp_plot = {'xlabel': "'time'",
                         'ylabel': "'current'",
                         'xlim': "[0, 200]",
                         'ylim': "[-.1,1]",
                         'title': "'Amperometry time course'",
                         'subplots_adjust': "bottom=0.15, left=0.12"}
        self.cv_plot = {'xlabel': "'voltage (mV)'",
                        'ylabel': "u'current (\u00B5A)'",
                        'title': "'Cyclic Voltammetry'",
                        'subplots_adjust': "bottom=0.15, left=0.12"}
        self.cv_canvas = {'xlabel': "voltage (mV)",
                          'ylabel': u"current (\u00B5A)",
                          'width': 600,
                          'height': 300,
                          'xlim': [-500, 500],
                          'ylim': [-1, 1],
                          'title': "Cyclic Voltammetry"}
        self.amp_canvas = {'xlabel': "time",
                           'ylabel': "current",
                           'width': 600,
                           'height': 300,
                           'xlim': [000, 200],
                           'ylim': [-1, 1],
                           'title': "Amperometry time course"}
