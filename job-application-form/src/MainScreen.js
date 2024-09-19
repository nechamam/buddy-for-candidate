import React from 'react';
import { Container, AppBar, Toolbar, Typography, Box, Button, Grid, Paper } from '@mui/material';
import { makeStyles } from '@mui/styles';
import JobApplicationForm from './JobApplicationForm'; // Import the modal component
import { LinkedIn as LinkedInIcon, Description as DescriptionIcon, Code as CodeIcon, Person as PersonIcon, CloudUpload as CloudUploadIcon, Help as HelpIcon, AccountCircle as AccountCircleIcon } from '@mui/icons-material';

const useStyles = makeStyles(() => ({
  root: {
    flexGrow: 1,
    fontFamily: 'Arial, sans-serif',
  },
  appBar: {
    backgroundColor: '#3f51b5',
  },
  logo: {
    flexGrow: 1,
  },
  section: {
    padding: '16px',
    textAlign: 'center',
    color: '#000',
  },
  button: {
    margin: '8px',
  },
  paper: {
    padding: '16px',
    textAlign: 'center',
    color: '#000',
    backgroundColor: '#f5f5f5',
  },
  icon: {
    fontSize: '50px',
    color: '#3f51b5',
  },
}));

const MainScreen = () => {
  const classes = useStyles();
  const [openModal, setOpenModal] = React.useState(false);

  const handleOpenModal = () => {
    setOpenModal(true);
  };

  const handleCloseModal = () => {
    setOpenModal(false);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" className={classes.logo}>
            <img src="logo.png" alt="Logo" style={{ height: '30px' }} />
          </Typography>
        </Toolbar>
      </AppBar>
      <Container>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paper}>
              <DescriptionIcon className={classes.icon} />
              <Typography variant="h6">Resume</Typography>
              <Button variant="contained" color="primary" className={classes.button} onClick={handleOpenModal} startIcon={<CloudUploadIcon />}>
                Upload Resume
              </Button>
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paper}>
              <CodeIcon className={classes.icon} />
              <Typography variant="h6">LeetCode Questions</Typography>
              <Button variant="contained" color="primary" className={classes.button}>
                View Scores
              </Button>
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paper}>
              <LinkedInIcon className={classes.icon} />
              <Typography variant="h6">LinkedIn Profile</Typography>
              <Button variant="contained" color="primary" className={classes.button} startIcon={<HelpIcon />}>
                Get Help
              </Button>
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Paper className={classes.paper}>
              <PersonIcon className={classes.icon} />
              <Typography variant="h6">User Profile</Typography>
              <Button variant="contained" color="primary" className={classes.button} startIcon={<AccountCircleIcon />}>
                View Details
              </Button>
            </Paper>
          </Grid>
        </Grid>
      </Container>
      <JobApplicationForm open={openModal} onClose={handleCloseModal} />
    </div>
  );
};

export default MainScreen;