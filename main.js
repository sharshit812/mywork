function main()
{
   var token;

   FB.getLoginStatus(function getLoginStatusCallback(response)
   {
      if (response.status === "connected")
      {
         document.getElementById("loginButton").style.display = "none";
      }
      else
      {
         document.getElementById("loginButton").style.display = "all";
      }
      token = response.authResponse.accessToken;

      console.log("token = " + token);

      Fb.api("/me", "get", token, function() {
      // this will work now.
      });

   }, true);
}
