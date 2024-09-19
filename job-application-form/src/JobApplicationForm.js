import React, { useState } from 'react';
import { Container, TextField, Button, Stepper, Step, StepLabel, Typography, Box, Modal, IconButton } from '@mui/material';
import { Close as CloseIcon, ArrowForward as ArrowForwardIcon, ArrowBack as ArrowBackIcon, Check as CheckIcon } from '@mui/icons-material';
import { makeStyles } from '@mui/styles';
import axios from 'axios';

const useStyles = makeStyles(() => ({
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  paper: {
    backgroundColor: '#fff',
    border: '2px solid #000',
    boxShadow: 24,
    padding: '16px',
    width: '80%',
    maxWidth: '600px',
  },
  stepper: {
    padding: '24px 0 40px',
  },
  button: {
    marginRight: '8px',
  },
  logo: {
    display: 'block',
    margin: '0 auto 20px',
  },
  vibrant: {
    backgroundColor: '#ff4081',
    color: '#fff',
  },
}));

const JobApplicationForm = ({ open, onClose }) => {
  const classes = useStyles();
  const [activeStep, setActiveStep] = useState(0);
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    current_position: '',
    looking_for_position: '',
    skills: '',
    phone_number: ''
  });

  const steps = ['Personal Information', 'Job Preferences'];

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/user-details', formData);
      console.log('Form submitted:', response.data);
      onClose();
    } catch (error) {
      console.error('Error submitting form:', error);
    }
  };

  return (
    <Modal
      open={open}
      onClose={onClose}
      className={classes.modal}
    >
      <div className={classes.paper}>
        <IconButton onClick={onClose} style={{ float: 'right' }}>
          <CloseIcon />
        </IconButton>
        <img src="logo.png" alt="D&I Logo" className={classes.logo} />
        <Typography variant="h4" align="center" gutterBottom>
          Job Application Form
        </Typography>
        <Stepper activeStep={activeStep} className={classes.stepper}>
          {steps.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>
        <div>
          {activeStep === steps.length ? (
            <div>
              <Typography variant="h5" gutterBottom>
                All steps completed
              </Typography>
              <Button onClick={handleSubmit} className={classes.vibrant} startIcon={<CheckIcon />}>
                Submit
              </Button>
            </div>
          ) : (
            <div>
              {activeStep === 0 && (
                <Box>
                  <TextField label="First Name" fullWidth margin="normal" name="first_name" value={formData.first_name} onChange={handleChange} />
                  <TextField label="Last Name" fullWidth margin="normal" name="last_name" value={formData.last_name} onChange={handleChange} />
                  <TextField label="Phone Number" fullWidth margin="normal" name="phone_number" value={formData.phone_number} onChange={handleChange} />
                </Box>
              )}
              {activeStep === 1 && (
                <Box>
                  <TextField label="Current Position" fullWidth margin="normal" name="current_position" value={formData.current_position} onChange={handleChange} />
                  <TextField label="Looking for Position" fullWidth margin="normal" name="looking_for_position" value={formData.looking_for_position} onChange={handleChange} />
                  <TextField label="Skills" fullWidth margin="normal" name="skills" value={formData.skills} onChange={handleChange} />
                </Box>
              )}
              <div>
                <Button
                  disabled={activeStep === 0}
                  onClick={handleBack}
                  className={classes.button}
                  startIcon={<ArrowBackIcon />}
                >
                  Back
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleNext}
                  className={classes.button}
                  endIcon={<ArrowForwardIcon />}
                >
                  {activeStep === steps.length - 1 ? 'Finish' : 'Next'}
                </Button>
              </div>
            </div>
          )}
        </div>
      </div>
    </Modal>
  );
};

export default JobApplicationForm;