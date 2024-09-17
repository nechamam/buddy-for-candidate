using Buddy.For.Candidate.Service.Models;
using Buddy.For.Candidate.Service.Services;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<UserDetailsDb>(opt => opt.UseInMemoryDatabase("UsersDetailsList"));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();
var app = builder.Build();


app.MapGet("/", () => "Hello World!");

app.MapPost("/user-details", async (UserDetails userDetails, UserDetailsDb db) =>
{
    if (string.IsNullOrEmpty(userDetails.FirstName) || string.IsNullOrEmpty(userDetails.PhoneNumber))
    {
        return Results.BadRequest("Invalid user details");
    }

    db.UsersDetails.Add(userDetails);
    await db.SaveChangesAsync();

    // call gpt-3 to generate a resume
    return Results.Created($"/user-details/{userDetails.Id}", userDetails);
});

app.MapGet("/user-details/{id}", async (Guid id, UserDetailsDb db) =>
    await db.UsersDetails.FindAsync(id)
        is UserDetails todo
        ? Results.Ok(todo)
        : Results.NotFound());





app.Run();