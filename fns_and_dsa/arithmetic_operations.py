num1 , num2 = 0
operation = 'add'

def perform_operation(num1,num2,operation):
    match(operation):
        case 'add':
            return num1+num2
        case 'subtract':
            return num2-num1
        case 'multiply':
            return num1*num2
        case 'divide':
            return num2/num1
        
