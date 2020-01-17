package com.example.demorabbitmq;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class Runner implements CommandLineRunner {

	@Autowired
	RabbitMQSender rabbitMQSender;

	 
    public Runner(RabbitMQSender rabbitMQSender) {
        this.rabbitMQSender = rabbitMQSender;
    }

    @Override
    public void run(String... args) {
        System.out.println("Sending message...");
        rabbitMQSender.send(new Message("Hello Message!",System.currentTimeMillis()));
    }

}