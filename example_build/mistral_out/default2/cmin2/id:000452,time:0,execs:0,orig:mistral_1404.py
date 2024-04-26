
import torch

def add_tensors(tensor1: torch.Tensor, tensor2: torch.Tensor):
    # Assert the shapes of input tensors are compatible for addition (broadcasting)
    assert tensor1.shape == tensor2.shape or \
           (len(torch.size(tensor1)) == len(torch.size(tensor2)) - 1 and
            torch.size(tensor1)[-1] is None), "Shapes are not compatible for addition"
    
    # Add tensors element-wise
    result = tensor1 + tensor2

    return result

# Create some input tensors
input_tensor1 = torch.randn((3, 4))
input_tensor2 = torch.randn((3, 4, 5))
input_tensor3 = torch.randn((3, 4))

try:
    # Add tensors with incompatible shapes
    result = add_tensors(input_tensor1, input_tensor2)
except AssertionError as e:
    print(f"Error message: {str(e)}")
else:
    print("Successfully added compatible tensors.")
    
# Add tensors with compatible shapes
output = add_tensors(input_tensor3, input_tensor3)
print(output.shape)
