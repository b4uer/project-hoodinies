import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: customBtn

    // Custom properties
    property color colorDefault: "#211747"
    property color colorMouseOver: "#31226b"
    property color colorPressed: "#5c0914"

    QtObject {
        id: internal
        property var dynamicColor: customBtn.down ? colorPressed : customBtn.hovered ? colorMouseOver : colorDefault
    }

    implicitWidth: 64
    implicitHeight: 32
    

    background: Rectangle {
        color: internal.dynamicColor
        radius: 4
    }

    contentItem: Item {
        id: item1
        Text {
            id: textBtn
            text: customBtn.text
            font.pixelSize: customBtn.font.pixelSize
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter
            color: "white"
        }
    }
}
 