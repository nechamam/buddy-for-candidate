using Buddy.For.Candidate.Service.Models;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.MapPost("/user-details", async (HttpContext context) =>
{
    var userDetails = await context.Request.ReadFromJsonAsync<UserDetails>();
    if (userDetails == null)
    {
        context.Response.StatusCode = StatusCodes.Status400BadRequest;
        await context.Response.WriteAsync("Invalid user details");
        return;
    }

    // Process the user details (e.g., save to database)
    // For demonstration, we'll just return the received details
    context.Response.StatusCode = StatusCodes.Status200OK;
    await context.Response.WriteAsJsonAsync(userDetails);
});

app.Run();