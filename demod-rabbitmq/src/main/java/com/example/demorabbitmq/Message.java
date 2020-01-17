package com.example.demorabbitmq;

 
public class Message {
	long date;
	String message;
	
	

	
	public long getDate() {
		return date;
	}

	public void setDate(long date) {
		this.date = date;
	}

	public Message( ) { 
	}
	
	public Message(String message,long date) {
		this.message = message;
		this.date = date;
	}

	public String getMessage() {
		return message;
	}

	public void setMessage(String message) {
		this.message = message;
	}
	
	public String toString() {
		return "{\"message\":\""+message+"\",\"date\":"+date+"}";
	}
	
}
