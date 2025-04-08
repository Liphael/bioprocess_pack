    def default_strategies(self):
        global current_path
        current_path = os.path.abspath(__file__)
        global f_path
        f_path = current_path + '\\default.csv'
        self.lineedit_path.setText(f_path)
        with open(f_path, encoding='utf8') as f:
            stra = strategy = pd.read_csv(
                f,
                encoding = 'utf8',
                sep = ',',
                header = 0,
                dtype = {'name':str,'type':str,'quantity':float,'unit':str},
                names = ['name','type','quantity','unit'],
                na_values = 'null',
                thousands = ',',
                decimal = '.',
            )
        f.close()
        stra_model = DataModel(stra)
        self.tableview_stra.setModel(stra_model)
        self.tableview_stra2.setModel(stra_model)

    def load_path(self):
        global current_path
        current_path = os.path.abspath(__file__)
        try:
            f_path = QFileDialog.getOpenFileName(
                self,
                'Open File',
                current_path,
                'CSV Files (*.csv)'
            )[0]
        except FileNotFoundError:
            log = log + '\\File not found!'
        self.lineedit_path.setText(f_path)


    def load_strategies(self):
        self.load_path()
        with open(f_path, encoding='utf8') as f:
            stra = strategy = pd.read_csv(
                f,
                encoding = 'utf8',
                sep = ',',
                header = 0,
                dtype = {'name':str,'type':str,'quantity':float,'unit':str},
                names = ['name','type','quantity','unit'],
                na_values = 'null',
                thousands = ',',
                decimal = '.',
            )
        f.close()
        stra_model = DataModel(stra)
        self.tableview_stra.setModel(stra_model)
        self.tableview_stra2.setModel(stra_model)