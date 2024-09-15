var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

var tasks = new List<TaskItem>
{
    new TaskItem(1, "Task 1", false),
    new TaskItem(2, "Task 2", true),
    new TaskItem(3, "Task 3", false)
};

app.MapGet("/", () => "Hello World!");

// GET endpoint with parameter in URL
app.MapGet("/tasks/{id}", (int id) =>
{
    var task = tasks.FirstOrDefault(t => t.Id == id);
    return task is not null ? Results.Ok(task) : Results.NotFound();
});
app.Run();
public record TaskItem(int Id, string Name, bool IsComplete);