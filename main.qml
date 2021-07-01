import QtQuick 2.15
import QtQuick.Controls 2.15
import "qml/controls"

ApplicationWindow {
    visible: true
    id: window
    visibility: "FullScreen"
    width: screen.width
    height: screen.height
    title: "project"
    property QtObject backend

    property string src: "./tmp/face_image_9.png"
    Component.onCompleted: img_photo.source = src

    Rectangle {
        anchors.fill: parent

        Image {    
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            //anchors.fill: parent
            source: "./images/background.jpg"
            fillMode: Image.PreserveAspectCrop
        }

        Rectangle {
            anchors.fill: parent
            color: "transparent"

            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: qsTr("Prototype")
                font.pixelSize: 48
                color: "white"
            }
        }
    
        
        Image {
            id: img_photo
            anchors {
                top: parent.top
                topMargin: 30
                right: parent.right
                rightMargin: 20
            }
            width: 720
            height: 460
            
            visible: false
            cache: false
        }

        Image {
            id: img_qrcode
            anchors {
                top: parent.top
                topMargin: 30
                left: parent.left
                leftMargin: 20
            }
            width: 300
            height: 300
            
            visible: false
            source: "./images/myqr.png"
        }

        CustomBtn {
            anchors {
                verticalCenter: parent.verticalCenter
                right: parent.right
                rightMargin: 25
            }
            text: qsTr("Photo")
            implicitWidth: 100
            implicitHeight: 50
            font.pixelSize: 20
            onClicked: {
            console.log("reloading")
            img_photo.source = ""
            img_photo.source = src
            img_photo.visible = true
            }
        }   

        CustomBtn {
            anchors {
                verticalCenter: parent.verticalCenter
                left: parent.left
                leftMargin: 25
            }
            text: qsTr("QRcode")
            implicitWidth: 100
            implicitHeight: 50
            font.pixelSize: 20
            onClicked: img_qrcode.visible = true
        }   

        CustomBtn {
            anchors {
                bottom: parent.bottom
                bottomMargin: 12
                right: parent.right
                rightMargin: 12
            }
            text: qsTr("Exit")
            font.pixelSize: 18
            onClicked: window.visibility = "Windowed"
        }   

        CustomBtn {
            anchors {
                verticalCenter: parent.verticalCenter
                horizontalCenter: parent.horizontalCenter
            }
            text: qsTr("Start")
            implicitWidth: 160
            implicitHeight: 80
            font.pixelSize: 40
            onClicked: {
                backend.start_process()
            }
        }  

        Connections {
            target: backend
        }
    }
}