def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string.')
    if not user_input:
        raise ValueError('Input cannot be empty.')
    if len(user_input) > 255:
        raise ValueError('Input exceeds maximum length of 255 characters.')
    return True

def main_processing_loop():
    while True:
        try:
            user_input = input('Enter your input: ')
            validate_input(user_input)
            # Process the valid input
            print('Processing:', user_input)
        except ValueError as e:
            print(f'Input error: {e}')
        except KeyboardInterrupt:
            print('\nExiting the loop.')
            break

if __name__ == '__main__':
    main_processing_loop()