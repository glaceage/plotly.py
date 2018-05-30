import _plotly_utils.basevalidators


class CategoryarraysrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='categoryarraysrc',
        parent_name='layout.scene.xaxis',
        **kwargs
    ):
        super(CategoryarraysrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )