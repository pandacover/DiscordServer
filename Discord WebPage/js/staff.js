function staffList() {
    const staffArray = ["ᴢ3ʀ0#3688: Moderator", "Yuma-Tsushima07#5724: Moderator"];
    for (index = 0; index < staffArray.length; index++) {
        var ul = document.getElementById("staff-list");
        var li = document.createElement("li");
        li.setAttribute('id',"staff");
        li.appendChild(document.createTextNode(staffArray[index]));
        ul.appendChild(li);
    }
}