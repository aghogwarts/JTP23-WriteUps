Searched in the usual places like header, inside the macro, all the slides, behind objects but did not find anything. While searching for other ways to hide data in .pptm files 
found this thread https://www.reddit.com/r/HowToHack/comments/zqinsq/any_way_to_hide_a_file_in_a_pptx_presentation_file/.

So used `mv` to change the file to a .zip and extracted it. Going through the contents found a file called hidden with charaters inside. Used multi-decoder and found the flag decoded 
from base64.


Flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
