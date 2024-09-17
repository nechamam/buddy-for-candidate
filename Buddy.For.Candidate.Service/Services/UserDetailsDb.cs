using Buddy.For.Candidate.Service.Models;
using Microsoft.EntityFrameworkCore;

namespace Buddy.For.Candidate.Service.Services
{
    public class UserDetailsDb : DbContext
    {
        public UserDetailsDb(DbContextOptions<UserDetailsDb> options)
            : base(options) { }

        public DbSet<UserDetails> UsersDetails => Set<UserDetails>();
    }
}
