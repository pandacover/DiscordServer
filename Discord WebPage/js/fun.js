function fun() {
    const command = ["dog", "cat"];
    const description = ["Returns a dog image with a dog fact. Aliases: pup, puppy!", "Returns a cat image with a cat fact. Aliases: neko, kitty!"];
    for (index = 0; index < command.length; index++) {
        var ul = document.getElementById("command-container");
        var li = document.createElement("li");
        li.setAttribute('id',"command-item");
        li.appendChild(document.createTextNode(command[index]+": "+description[index]));
        ul.appendChild(li);
    }
}