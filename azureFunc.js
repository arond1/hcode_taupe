   module.exports = async function (context, req) {
      context.log('JavaScript HTTP trigger function processed a request.');
  
      const request = require('request')

      if (req.query.first_name && req.query.last_name) {
        request.post('https://wa-devoir-esgi.azurewebsites.net/api/user/create', {
              headers: {
                  "content-type": "application/json",
              },
              body: {
                  "first_name": req.query.first_name,
                  "last_name": req.query.last_name
              }
              }, (error, res, body) => {
              if (error) {
                  console.error(error)
                  return
              }
              console.log(`statusCode: ${res.statusCode}`)
              console.log(body)
        })
        } else {
            context.res = {
                status: 400,
                body: "Please pass a name on the query string or in the request body"
            };
        }
  };
