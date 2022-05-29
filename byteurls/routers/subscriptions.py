# router.post("/subscribe", function(req, res, next) {
#   const { name, email } = req.body;

#   // 1. Validate the user data
#   // 2. Subscribe the user to the mailing list
#   // 3. Send a confirmation email

#   res.render("subscribed", {
#     title: "You are subscribed",
#     name,
#     email
#   });
# });



