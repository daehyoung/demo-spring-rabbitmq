package com.example.demorabbitmq;


import org.springframework.amqp.core.AmqpTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
 

@Service
public class RabbitMQSender {
	
	@Autowired
	private AmqpTemplate rabbitTemplate;
	
	@Value("${app.rabbitmq.exchange}")
	private String exchange;
	
	@Value("${app.rabbitmq.routingkey}")
	private String routingkey;	
	
	public void send(Message msg) {
		
		rabbitTemplate.convertAndSend(exchange, routingkey, msg);
		System.out.println("exchange:" + exchange+",routingkey:"+routingkey);
		System.out.println("Send msg = " + msg);
	    
	}
}