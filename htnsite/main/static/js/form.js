var firebaseConfig = {
    apiKey: "AIzaSyCzUoMG6eGiGR_On-9YbH5WduTMQKo56Kg",
    authDomain: "htn2020-dd0be.firebaseapp.com",
    databaseURL: "https://htn2020-dd0be-default-rtdb.firebaseio.com",
    projectId: "htn2020-dd0be",
    storageBucket: "htn2020-dd0be.appspot.com",
    messagingSenderId: "451004304763",
    appId: "1:451004304763:web:b29bf7a32716f1a15281de"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
database = firebase.database();

let dataInfo = firebase.database().ref("newDataset")

function submitForm() {
    console.log(123);
    let title = document.getElementById('datasetName').value;
    let company = document.getElementById('companyName').value;
    let description = document.getElementById('description').value;
    let requiredData = document.getElementById('requiredData');
    var checkText = requiredData.options[requiredData.selectedIndex].text;
    console.log(title);
    console.log(company);
    console.log(description);
    console.log(checkText);
    saveDataInfo(title,company,description,checkText);
}

function saveDataInfo(title, company, description,checkText) {
    let newDataInfo = dataInfo.push();

    newDataInfo.set({
        DataSetTitle:title,
        DataSetCompany:company,
        DataSetDescription:description,
        DataSetCheckText:checkText
    })
}

var leadsRef = database.ref('newDataset');
leadsRef.on('value', function(snapshot) {
    snapshot.forEach(function(childSnapshot) {
      var childData = childSnapshot.val();
      console.log(childData);
      createCard(childData.DataSetTitle,childData.DataSetCompany,childData.DataSetDescription,childData.DataSetCheckText);
    });
});


function createCard(dataTitle, dataName, dataDesc,dataType) {
    console.log("new card");
    var element= document.getElementById("card");
    var clone = element.cloneNode(true);
    clone.id="newCard"
    console.log(clone.id.tag);
    document.getElementById('title').innerHTML = dataTitle;
    document.getElementById('desc').innerHTML = dataDesc;
    document.getElementById('tag').innerHTML = dataType;
    element.after(clone);
}
//document.getElementById("p1").innerHTML = "New text!";