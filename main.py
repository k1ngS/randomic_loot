import sys
import random
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from lootTable import LootTable
from enchantedItem import EnchantedItem


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.loot_table = LootTable()
        self.enchanted_item = EnchantedItem()

        self.setWindowTitle('Loot Generator')
        self.setStyleSheet("background-color: gray;")
        self.width = 800
        self.height = int(0.618 * self.width)
        self.setFixedSize(self.width, self.height)

        self.btn_1 = QPushButton('Loot', self)
        self.btn_2 = QPushButton('Lista de Feitiços', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)

        self.tab1 = self.ui1()
        self.tab2 = self.ui2()

        self.initUI()

    # Checkbox "+bau?"
    def toggle_num_chests_input(self, state):
        if state == Qt.Checked:
            self.num_chests_input.setHidden(False)
        else:
            self.num_chests_input.setHidden(True)

    # Sidebar
    def initUI(self):
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.btn_1)
        leftLayout.addWidget(self.btn_2)
        leftLayout.addStretch(5)
        leftLayout.setSpacing(20)
        leftWidget = QWidget()
        leftWidget.setLayout(leftLayout)

        self.rightWidget = QTabWidget()
        self.rightWidget.tabBar().setObjectName('mainTab')

        self.rightWidget.addTab(self.tab1, '')
        self.rightWidget.addTab(self.tab2, '')

        self.rightWidget.setCurrentIndex(0)
        self.rightWidget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        mainLayout = QHBoxLayout()
        mainLayout.addWidget(leftWidget)
        mainLayout.addWidget(self.rightWidget)
        mainLayout.setStretch(0, 40)
        mainLayout.setStretch(1, 200)
        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

    # Botões da SideBar
    def button1(self):
        self.rightWidget.setCurrentIndex(0)

    def button2(self):
        self.rightWidget.setCurrentIndex(1)

    # Pages
    def ui1(self):
        self.num_chests = 1

        controlsLayout = QHBoxLayout()
        gridLayout = QGridLayout()
        groupBox = QGroupBox()

        self.show_chest_checkbox = QCheckBox("+bau?")
        self.show_chest_checkbox.stateChanged.connect(
            self.toggle_num_chests_input)
        controlsLayout.addWidget(self.show_chest_checkbox)

        self.num_chests_input = QSpinBox()
        self.num_chests_input.setValue(self.num_chests)
        self.num_chests_input.resize(100, 10)
        self.num_chests_input.setHidden(True)
        controlsLayout.addWidget(self.num_chests_input)

        self.dice_combo = QComboBox()
        self.dice_combo.addItems(["d6", "d8", "d10", "d12", "d20"])
        controlsLayout.addWidget(self.dice_combo)

        self.roll_button = QPushButton("Rolar")
        self.roll_button.clicked.connect(self.roll_dice)
        controlsLayout.addWidget(self.roll_button)

        self.result_label = QLabel("Loot")
        self.result_label.setFont(QtGui.QFont('', 16))
        gridLayout.addWidget(self.result_label)

        controls = QWidget()
        controls.setLayout(controlsLayout)
        groupBox.setLayout(gridLayout)

        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        self.result_label.setWordWrap(True)
        self.result_label.setAlignment(Qt.AlignJustify)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(controls)
        mainLayout.addWidget(scroll)
        main = QWidget()
        main.setLayout(mainLayout)
        return main

    def ui2(self):

        heading = QtGui.QFont('', 12)
        heading.setBold(True)

        title = QLabel('Lista de Feitiços')
        title.setFont(heading)
        title.setAlignment(Qt.AlignJustify)

        groupBox = QGroupBox()
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(title)
        main = QWidget()
        main.setLayout(mainLayout)
        return main

    # Generate Items
    def roll_dice(self):
        self.num_chests = int(self.num_chests_input.text())
        result = []
        for i in range(self.num_chests):
            dice = int(self.dice_combo.currentText()[1:])
            roll = random.randint(1, 6)
            if roll == 5:
                item = self.loot_table.loot_table[roll]
                if type(item) is dict:
                    spell_choice = random.randint(1, 6)
                    spell = self.loot_table.loot_table[5]['feiticos'][spell_choice]
                    result.append(spell)
                else:
                    result.append(roll)
            elif roll == 6:
                item = self.loot_table.loot_table[roll]
                if type(item) is dict:
                    forma = random.randint(1, 20)
                    enchanted_item = self.enchanted_item.generate_enchanted_item(
                        self.loot_table.loot_table[6]['forma'][forma])
                    result.append(enchanted_item)
                else:
                    result.append(roll)
            else:
                result.append(self.loot_table.loot_table[roll])
        self.result_label.setText("\n".join(result))

        with open("loots.txt", "w") as f:
            f.write('Loots\n')
            f.write("\n".join(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
