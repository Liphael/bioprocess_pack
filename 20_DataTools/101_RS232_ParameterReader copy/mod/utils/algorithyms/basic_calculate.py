class basic_calculate():
    def cal(self, parent):
        global be_vol, sa_vol, af_vol
        be_vol = sa_vol = af_vol = 0  # 给予初始化0值，以防计算问题

        be_vol = before_volume = float(MainWindowUi.ui.spinbox_before_sampling.value())
        sa_vol = sample_volume = float(MainWindowUi.ui.spinbox_sampling.value())

        ## calculate the feed volume
        af_vol = after_volume = be_vol - sa_vol
        return be_vol, sa_vol, af_vol
