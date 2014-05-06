Contact = Backbone.Model.extend({

	urlRoot: "/api/v1/contact/",

	initialize: function() {
		console.log('contact model has been initialized');

		this.on("change", function() {
			console.log("Attributes in this Model have changed");
			console.log(this.toJSON());
		});
	},

	defaults: {
      name: '',
      email: '',
      message: '',
    },

	setName: function(thename) {
		this.set({name: thename});
	},

	setEmail: function(email) {
		this.set({email: email});
	},

	setMessage: function(message) {
		this.set({message: message});
	},

});


var name = $('#contact-name').val();
var email = $('#contact-mail').val();
var message = $('#contact-message').val();

$('#contact-send').click(function() {
	var contact = new Contact();

	contact.set({ "name": name, "email": email, "message": message });
	contact.save();
});